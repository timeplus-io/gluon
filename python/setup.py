# coding: utf-8

"""
    Timeplus
    OpenAPI spec version: 1.0.0-oas3
    Contact: support@timeplus.com
"""

from setuptools import setup, find_packages  # noqa: H301
import os

print("current dir")
print(os.getcwd())

exec(open("timeplus/version.py").read())

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = [
    "urllib3 >= 1.15",
    "six >= 1.10",
    "certifi",
    "sseclient-py>=1.7.2",
    "loguru>=0.6.0",
    "sqlalchemy>=1.4.36",
    "python-dateutil",
]

setup(
    name="timeplus",
    version=__version__,  # noqa: F821
    author="Gang Tao",
    author_email="gang@timeplus.io",
    description="Timeplus python SDK",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/timeplus-io/gluon/tree/develop/python",
    packages=find_packages(where="timeplus", exclude=("tests",)),
    install_requires=requirements,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.9",
    ],
)
