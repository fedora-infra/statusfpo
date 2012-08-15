#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import gmtime, strftime
import argparse
import sys
import json
import datetime
from jinja2 import Environment, FileSystemLoader

def getInfo(filename):
    f = open(filename, 'r')
    info = json.loads(f.read())
    f.close()
    return info

def generateFeedPage(feedtype, changes):
    env = Environment(loader=FileSystemLoader('.'))
    newchanges = []
    for change in changes:
        change['datetime'] = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(change['changedate']))
        newchanges.append(change)
    return env.get_template(feedtype).render(changes=changes, currenttime=strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))

def generateHtmlPage(statuses):
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

def generateHtml():
    return generateHtmlPage(getInfo('statuses.json'))

def generateFeed(feedtype):
    return generateFeedPage(feedtype + '.html', getInfo('changes.json'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate the static files')
    parser.add_argument('type', help='The type of page to generate, either html or rss')
    args = parser.parse_args()

    if args.type == 'html':
       print(generateHtml())
    elif args.type == 'rss':
       print(generateFeed('rss'))
    else:
        print('Error: invalid type (html/rss)')
        sys.exit(1)
