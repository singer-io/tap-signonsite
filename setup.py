#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="tap-signonsite",
    version="0.0.1",
    description="Singer.io tap for extracting data from the SignOnSite API",
    python_requires=">=3.6.0",
    author="Sam Woolerton",
    url="https://samwoolerton.com",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_signonsite"],
    install_requires=["singer-python==5.9.0", "requests==2.20.0"],
    extras_require={"dev": ["pylint", "ipdb", "nose",]},
    entry_points="""
          [console_scripts]
          tap-signonsite=tap_signonsite:main
      """,
    packages=["tap_signonsite"],
    package_data={"tap_signonsite": ["tap_signonsite/schemas/*.json"]},
    include_package_data=True,
)
