#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = []

setup_requirements = ["setuptools-scm"]

test_requirements = ["pytest"]

dev_requirements = ["black", "flake8", "isort", "pre-commit"]
dev_requirements += requirements

setup(
    author="Ivan Ogasawara",
    author_email="ivan.ogasawara@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Project for the jam session with python",
    install_requires=requirements,
    extras_require={"dev": dev_requirements},
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="jam_session_python",
    name="jam_session_python",
    packages=find_packages(include=["jam_session_python"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/xmnlab/jam_session_python",
    use_scm_version=True,
    zip_safe=False,
)
