#! /usr/bin/env python
# Copyright 2015 Jan Markup <mhmcze@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

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
