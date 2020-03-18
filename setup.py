#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name="vehicle_control",
    version="0.1",
    author="Andrea Conti",
    author_email="andrea.conti@tutanota.com",
    description="software to control a vehicle with 2 motors",
    long_description=open('README.md').read(),
    package_dir={'': 'src'},
    packages=find_packages(),
    # package_data={'': ['*.dat', '*.csv']},
    entry_points={
        'console_scripts': [
            'vehicle_control = vehicle_control.__main__:main'
        ]
    },
    tests_require=[
        'pytest'
    ],
    install_requires=[
        'gpiozero',
        'flask',
        'argparse'
    ]
)
