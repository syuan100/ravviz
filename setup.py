from setuptools import setup, find_packages

setup(
    name='ravviz',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "flask",
        "flask-sqlalchemy==2.4.4"
    ],
    dependency_links=[
        "https://github.com/ravenprotocol/ravcom.git@0.1-alpha",
        "https://github.com/ravenprotocol/ravop.git@0.1-alpha"
    ]
)
