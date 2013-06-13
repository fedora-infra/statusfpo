#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# Fedora-status, a set of scripts generating a service status overview.
# Copyright (C) 2012  Red Hat, Inc., Patrick Uiterwijk
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from time import time
import json
import argparse
import sys
import subprocess
import os

from util_functions import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manage the status on status.fedoraproject.org')
    parser.add_argument('new_status', help='The new service status (good/scheduled/minor/major)')
    parser.add_argument('new_message', help='The new status message. Use - to use "Everything seems to be working"')
    parser.add_argument('service', help='The service(s) to modify. Use - to update every service', nargs='+')
    parser.add_argument('--no-git', action='store_true', help='Do not commit and push to git')
    parser.add_argument('--global-info', help='Set the global information message')
    args = parser.parse_args()

    if not args.new_status in ['good', 'scheduled', 'minor', 'major']:
        print('new_status must be good, scheduled, minor or major!')
        sys.exit(1)

    if '-' in args.service and len(args.service) != 1:
        print('Please only specify services or -, not both')
        sys.exit(1)

    if args.new_message == '-':
        args.new_message = 'Everything seems to be working.'

    result = 0

    if not args.no_git:
        if not os.path.isdir('.git'):
            print("We couldn't find a .git directory, so forcing --no-git")
            args.no_git = True
        else:
            result = subprocess.call("git pull", shell=True)
    if result != 0:
        print('An error occured in git pull, please try again!')
        sys.exit(2)

    f = open('.fsrootdir/statuses.json', 'r')
    services = json.loads(f.read())
    f.close()
    f = open('.fsrootdir/changes.json', 'r')
    changes = json.loads(f.read())
    f.close()

    for srvc in args.service:
        if (srvc != '-') and (not srvc in services['services'].keys()):
            print('%(service)s is unknown! Valid services are: %(services)s' % {'service': srvc, 'services': services['services'].keys()})
            sys.exit(3)

    if args.global_info != None:
        services['global_info'] = args.global_info

    updated = []
    if args.service == '-':
        for srv in services['services'].keys():
            if services['services'][srv]['status'] != args.new_status or services['services'][srv]['message'] != args.new_message:
                updated.append(srv)
            services['services'][srv]['status'] = args.new_status
            services['services'][srv]['message'] = args.new_message
    else:
        for srvc in args.service:
            if services['services'][srvc]['status'] != args.new_status or services['services'][srvc]['message'] != args.new_message:
                updated.append(srvc)
            services['services'][srvc]['status'] = args.new_status
            services['services'][srvc]['message'] = args.new_message

    if len(updated) != 0:
        if len(updated) == 1:
            changes.insert(0, {'changetype': 'single', 'service': updated[0], 'status': args.new_status, 'new_global_status': getGlobalStatus(services['services']), 'message': args.new_message, 'changedate': time()})
        else:
            changes.insert(0, {'changetype': 'multiple', 'services': updated, 'status': args.new_status, 'new_global_status': getGlobalStatus(services['services']), 'message': args.new_message, 'changedate': time()})
    #changes = changes[:10]	# Trim the RSS feed to 10 entries

    f = open('.fsrootdir/statuses.json', 'w')
    f.write(json.dumps(services, sort_keys=True, indent = 4))
    f.close()
    f = open('.fsrootdir/changes.json', 'w')
    f.write(json.dumps(changes, indent = 4))
    f.close()

    if not args.no_git:
        result = subprocess.call("git add -A", shell=True)
    if result != 0:
        print('An error occured in git add, please try again!')
        sys.exit(4)

    if not args.no_git:
        if args.service == '-':
            result = subprocess.call('git commit -m "New service status for all services: %(newstatus)s, with message: %(message)s"' % {'service': args.service, 'newstatus': args.new_status, 'message': args.new_message}, shell=True)
        else:
            result = subprocess.call('git commit -m "New service status for %(service)s: %(newstatus)s, with message: %(message)s"' % {'service': args.service, 'newstatus': args.new_status, 'message': args.new_message}, shell=True)
    if result != 0:
        print('An error occured in git commit, please try again!');
        sys.exit(5)

    if not args.no_git:
        result = subprocess.call('git push origin master', shell=True)
    if result != 0:
        print('An error occured during git push, please try again!')
        sys.exit(6)
