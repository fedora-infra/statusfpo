#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import argparse
import sys
import subprocess

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manage the status on status.fedoraproject.org')
    parser.add_argument('service', help='The service to modify. Use - to update every service')
    parser.add_argument('new_status', help='The new service status (good/minor/major)')
    parser.add_argument('new_message', help='The new status message. Use - to use "Everything seems to be working"')
    parser.add_argument('--no-git', action='store_true', help='Do not commit and push to git')
    parser.add_argument('--global-info', help='Set the global information message')
    args = parser.parse_args()

    if not args.new_status in ['good', 'minor', 'major']:
        print('new_status must be good, minor or major!')
        sys.exit(1)

    if args.new_message == '-':
        args.new_message = 'Everything seems to be working'

    result = 0

    if not args.no_git:
        result = subprocess.call("git pull", shell=True)
    if result != 0:
        print('An error occured in git pull, please try again!')
        sys.exit(2)

    f = open('wsgi/statuses.json', 'r')
    services = json.loads(f.read())
    f.close()

    if (args.service != '-') and (not args.service in services['services'].keys()):
        print('%(service)s is unknown! Valid services are: %(services)s' % {'service': args.service, 'services': services['services'].keys()})
        sys.exit(3)

    if args.global_info != None:
        services['global_info'] = args.global_info

    if args.service == '-':
        for srv in services.keys():
            services['services'][srv]['status'] = args.new_status
            services['services'][srv]['message'] = args.new_message
    else:
        services['services'][args.service]['status'] = args.new_status
        services['services'][args.service]['message'] = args.new_message

    f = open('wsgi/statuses.json', 'w')
    f.write(json.dumps(services, sort_keys=True, indent = 4))
    f.close()

    if not args.no_git:
        result = subprocess.call("git add wsgi/statuses.json", shell=True)
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
