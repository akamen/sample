import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="blackduck_sample_project",
    version="0.0.2",
    author="Black Duck Software",
    author_email="",
    description=("A sample project for using the bdsplugin"),
    license="Apache 2.0",
    keywords="sample example blackduck bdsplugin",
    url="https://github.com/blackducksoftware/bdsplugin",
    packages=[],
    install_requires=["bdsplugin", "Delorean", "pynamodb"],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache 2.0 License",
    ],
    entry_points={"distutils.commands": [
        "bdio = bdsplugin.BlackDuckPlugin:BlackDuckCommand"]}
)

# from bdsplugin import BlackDuckPlugin
# pkgs = BlackDuckPlugin.get_setup_dependencies("blackduck_sample_project==0.0.1
# pkg = pkgs.pop(0)
