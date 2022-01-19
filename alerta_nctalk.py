import logging
import os
from hashlib import sha256
from secrets import token_bytes
import requests

try:
    from alerta.plugins import app  # alerta >= 5.0
except ImportError:
    from alerta.app import app  # alerta < 5.0
from alerta.plugins import PluginBase

LOG = logging.getLogger("alerta.plugins.nctalk")

NEXTCLOUD_SERVER = os.environ.get("NEXTCLOUD_SERVER") or app.config["NEXTCLOUD_SERVER"]
NEXTCLOUD_TALK_TOKEN = (
    os.environ.get("NEXTCLOUD_TALK_TOKEN") or app.config["NEXTCLOUD_TALK_TOKEN"]
)
NEXTCLOUD_USERNAME = (
    os.environ.get("NEXTCLOUD_USERNAME") or app.config["NEXTCLOUD_USERNAME"]
)
NEXTCLOUD_PASSWORD = (
    os.environ.get("NEXTCLOUD_PASSWORD") or app.config["NEXTCLOUD_PASSWORD"]
)
DASHBOARD_URL = os.environ.get("DASHBOARD_URL") or app.config.get("DASHBOARD_URL", "")
SEVERITY_ICON = {
    "critical": "🔴 ",
    "warning": "⚠ ",
    "ok": "✅ ",
    "cleared": "✅ ",
    "normal": "✅ ",
}


class SendMessage(PluginBase):
    def pre_receive(self, alert):
        return alert

    def post_receive(self, alert):

        if alert.repeat:
            return

        severity = SEVERITY_ICON.get(alert.severity, "")

        body = "{}{}: {} alert for {} \n{} - {} - {} \n{} \nDate: {} | {}/#/alert/{}".format(
            severity,
            alert.environment,
            alert.severity.capitalize(),
            ",".join(alert.service),
            alert.resource,
            alert.event,
            alert.value,
            alert.text,
            alert.create_time,
            DASHBOARD_URL,
            alert.id,
        )

        headers = {"Content-Type": "application/json", "OCS-APIRequest": "true"}

        payload = {
            "message": body,
            "referenceId": sha256(token_bytes(256)).hexdigest(),
        }

        LOG.debug("NC Talk: %s", payload)

        try:
            r = requests.post(
                f"{NEXTCLOUD_SERVER}/ocs/v2.php/apps/spreed/api/v1/chat/{NEXTCLOUD_TALK_TOKEN}",
                json=payload,
                headers=headers,
                auth=(NEXTCLOUD_USERNAME, NEXTCLOUD_PASSWORD),
                timeout=2,
            )
        except Exception as e:
            raise RuntimeError("NC Talk: ERROR - %s" % e)

        LOG.debug("NC Talk: %s - %s", r.status_code, r.text)

    def status_change(self, alert, status, text):
        return
