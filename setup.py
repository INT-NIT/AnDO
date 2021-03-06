#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

import re

verstr = "unknown"
try:
    verstrline = open('_version.py', "rt").read()
except EnvironmentError:
    pass # Okay, there is no version file.
else:
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1)
    else:
        raise RuntimeError("unable to find version in yourpackage/_version.py")



setup(
    name="AnDOChecker",
    version=verstr,
    packages=find_packages(),
    package_data={
            # If any package contains *.json or *.csv files, include them:
            "": ["*.json", '*.csv'],
    },
    author="Jeremy Garcia, Sylvain Takerkart",
    description="Checks the validity of a directory with respect to the ANimal Data Organization (ANDO) specifications ",
    license='MIT',
    install_requires=['flake8'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['AnDOChecker=ando.checker:main',
                            'AnDOGenerator=tools.generator.AnDOGenerator:main',
                            'AnDOViewer=tools.viewer.AnDOViewer:main'],
    },
    python_requires='>=3.6',
    extras_require={
        'tools': ['pandas'],
        'test': ['pytest']
    }
)
