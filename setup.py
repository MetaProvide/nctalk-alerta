from setuptools import setup, find_packages

version = "0.1.0"

setup(
    name="alerta-nctalk",
    version=version,
    description="Alerta plugin for Nextcloud Talk",
    url="https://github.com/MetaProvide/nctalk-alerta",
    license="MIT",
    author="Magnus Walbeck",
    author_email="mw@mwalbeck.org",
    packages=find_packages(),
    py_modules=["alerta_nctalk"],
    install_requires=["requests"],
    include_package_data=True,
    zip_safe=True,
    entry_points={"alerta.plugins": ["nctalk = alerta_nctalk:SendMessage"]},
)
