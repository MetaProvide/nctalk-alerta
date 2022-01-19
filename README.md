Nextcloud Talk Plugin
===================

Send Nextcloud Talk messages for new alerts.

Installation
------------

Clone the GitHub repo and run:

    $ python setup.py install

Or, to install remotely from GitHub run:

    $ pip install git+https://github.com/MetaProvide/nctalk-alerta.git

Note: If Alerta is installed in a python virtual environment then plugins
need to be installed into the same environment for Alerta to dynamically
discover them.

Configuration
-------------

Add `nctalk` to the list of enabled `PLUGINS` in `alertad.conf` server
configuration file and set plugin-specific variables either in the
server configuration file or as environment variables.

```python
PLUGINS = ['nctalk']
NEXTCLOUD_SERVER = ''       # default="not set"
NEXTCLOUD_TALK_TOKEN = ''   # default="not set"
NEXTCLOUD_USERNAME = ''     # default="not set"
NEXTCLOUD_PASSWORD = ''     # default="not set"
```

The `DASHBOARD_URL` setting should be configured to link Nextcloud Talk messages to
the Alerta console:

```python
DASHBOARD_URL = ''  # default="not set"
```

**Example**

```python
PLUGINS = ['reject','nctalk']
NEXTCLOUD_SERVER = 'https://cloud.example.com'
NEXTCLOUD_TALK_TOKEN = 'tfgwmh7s'
NEXTCLOUD_USERNAME = 'test'
NEXTCLOUD_PASSWORD = 'SNN5j-wE46R-G2Pei-QtRTf-9qFiJ'
DASHBOARD_URL = 'https://try.alerta.io'
```

References
----------

  * Nextcloud Talk API Docs: https://nextcloud-talk.readthedocs.io/en/latest/chat/#sending-a-new-chat-message

License
-------

Copyright (c) 2022 Magnus Walbeck. Available under the MIT License.
