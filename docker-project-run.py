#! /usr/bin/env python
# Copyright 2014 Jan Markup <mhmcze@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import glob
import os
import sys

if not os.geteuid() == 0:
    sys.exit('You must be root to run this application, please use sudo and try again.')

PATHS = ['.'];

for path in PATHS:
    path = os.path.abspath(path)
    projects = glob.glob(path + '/*/docker-compose.yml')
    if projects:
        print '--- ' + os.path.basename(path) + ' ---'
        for project in projects:
            print os.path.basename(os.path.dirname(project))

project = raw_input('>>> ')

for path in PATHS:
    compose = glob.glob(path + '/' + project + '/docker-compose.yml')
    if compose:
        projectDir = os.path.dirname(compose[0])
        os.system('cd "' + projectDir + '" && docker-compose up -d')
    else:
        print 'Project not found.'
