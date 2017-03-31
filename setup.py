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
    version="0.0.8",
    author="Black Duck Software",
    author_email="",
    description=("A sample project for using the hub-pip"),
    license="Apache 2.0",
    keywords="sample example blackduck hub-pip",
    url="https://github.com/blackducksoftware/hub_python_plugin",
    packages=[],
    install_requires=["Delorean", "pynamodb"],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache 2.0 License",
    ],
    entry_points={"distutils.commands": [
        "bdio = hub_pip.BlackDuckPlugin:BlackDuckCommand"]}
)
