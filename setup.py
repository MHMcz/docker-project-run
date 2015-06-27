#! /usr/bin/env python
from distutils.core import setup
import os
import shutil

if not os.path.exists('build'):
    os.makedirs('build')

shutil.copyfile('docker-project-run.py', 'build/docker-project-run')

setup(
    scripts = [
        'build/docker-project-run'
    ]
)
