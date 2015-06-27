#! /usr/bin/env python
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
        os.system('cd "' + projectDir + '" && docker-compose up')
    else:
        print 'Project not found.'
