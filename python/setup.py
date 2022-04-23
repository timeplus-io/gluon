from setuptools import setup, find_packages
import os

print("current dir")
print(os.getcwd())

exec(open("timeplus/version.py").read())

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="timeplus",
    version=__version__,  # noqa: F821
    author="Gang Tao",
    author_email="gang@timeplus.io",
    description="Timeplus python SDK",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/timeplus-io/gluon/python",
    packages=find_packages(where="timeplus", exclude=("tests",)),
    install_requires=requirements,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
