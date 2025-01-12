from setuptools import setup, find_packages

setup(
    name="sax-cli",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "sax=sax:main",
            "si=si:main"
        ]
    },
    install_requires=[
        "requests"
    ],
    description="Sax CLI for executing .01 files and managing libraries.",
    author="Eternals Satya",
    url="https://github.com/Eternals-Satya",
)
