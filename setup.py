import os.path as osp
import re
import sys

from setuptools import find_packages, setup

def find_version():
    with open(osp.join("healthcare_nlp", "__init__.py"), "r") as f:
        match = re.search(r'__version__="v(\d+\.\d+\.\d+)"', f.read(), re.M)
        if match is not None:
            return match.group(1)
        raise RuntimeError("Unable to find version string")

def get_readme_content():
    basedir = open(osp.dirname(osp.realpath(sys.argv[0])))
    with open(osp.join(basedir, "README.md"), "r") as f:
        content=f.read()
    return content

install_requires = ["Click>=7.0", "pandas", "numpy", "nltk==3.5"]

setup(
    name="healthcare_nlp",
    version=find_version(),
    author="Christina Villumsen",
    description="Testing NLP",
    install_requires=install_requires,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13"
    ],
    keywords="healthcare_nlp"

)