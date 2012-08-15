#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from jinja2 import Environment, FileSystemLoader

def getStatuses():
    f = open('statuses.json', 'r')
    services = json.loads(f.read())
    f.close()
    return services

def generatePage(statuses):
    env = Environment(loader=FileSystemLoader('.'))
    return env.get_template('template.html').render(statuses=statuses['services'], global_status=getGlobalStatus(statuses['services']), global_info=statuses['global_info'])

def getGlobalStatus(statuses):
    global_status = 0    # 0 = ok, 1 = minor, 2 = major
    for service in statuses.keys():
        status = statuses[service]['status']
        if status == 'minor' and global_status < 1:
            global_status = 1
        elif status == 'major' and global_status < 2:
            global_status = 2
    if global_status == 0:
        return 'ok'
    elif global_status == 1:
        return 'minor'
    else:
        return 'major'

def main():
    return generatePage(getStatuses())

if __name__ == '__main__':
    print(main())
