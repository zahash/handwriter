# python3 setup.py sdist bdist_wheel
# bumpversion --current-version <__version__> (major|minor|patch) setup.py

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

with (HERE / "requirements.txt").open() as f:
    requirements = f.read().splitlines()

# This call to setup() does all the work
setup(
    name="handwriter",
    version="0.0.1",
    description="Text to Handwriting converter",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/zahash/handwriter",
    author="zahash",
    author_email="zahash.z@gmail.com",
    license="AGPLv3",
    classifiers=[
        "License :: OSI Approved :: AGPLv3 License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["handwriter"],
    include_package_data=True,
    install_requires=requirements,
)