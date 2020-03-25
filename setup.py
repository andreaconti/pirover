#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name="pirover",
    version="0.1",
    author="Andrea Conti",
    author_email="andrea.conti@tutanota.com",
    description="software to control a rover with 2 motors, a camera and some other stuff",
    long_description=open('README.md').read(),
    package_dir={'': 'src'},
    packages=find_packages(),
    # package_data={'': ['*.dat', '*.csv']},
    entry_points={
        'console_scripts': [
            'pirover = pirover.__main__:main'
        ]
    },
    tests_require=[
        'pytest'
    ],
    install_requires=[
        'gpiozero',
        'flask',
        'argparse',
        'pigpio',
        'pillow',
        'numpy',
        # picamera: tested at runtime
    ]
)
