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

from time import gmtime, strftime
import argparse
import sys
import json
import datetime
from jinja2 import Environment, FileSystemLoader

def getVerboseStatus(global_status):
    if global_status == "good":
        return "All systems go"
    elif global_status == "scheduled":
        return "There are scheduled downtimes in progress"
    elif global_status == "minor":
        return "Minor service disruption"
    elif global_status == "major":
        return "Major service disruption"

def getInfo(filename):
    f = open(filename, 'r')
    info = json.loads(f.read())
    f.close()
    return info

def generateFeedPage(feedtype, changes, statuses):
    env = Environment(loader=FileSystemLoader('.'))
    newchanges = []
    for change in changes:
        change['datetime'] = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(change['changedate']))
        newchanges.append(change)
        if change['changetype'] == 'single':
            change['service'] = statuses['services'][change['service']]['name']
        else:
            change['serviceNames'] = []
            for srv in change['services']:
                change['serviceNames'].append(statuses['services'][srv]['name'])
    global_status = getVerboseStatus(getGlobalStatus(statuses['services']))
    return env.get_template(feedtype).render(changes=changes, currenttime=strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()), update_title=global_status)

def generateHtmlPage(statuses):
    env = Environment(loader=FileSystemLoader('.'))
    global_status = getVerboseStatus(getGlobalStatus(statuses['services']))
    return env.get_template('template.html').render(statuses=statuses['services'], global_status=getGlobalStatus(statuses['services']), global_info=statuses['global_info'], verbose_global_status=global_status)

def getGlobalStatus(statuses):
    global_status = 0    # 0 = ok, 1 = scheduled, 2 = minor, 3 = major
    for service in statuses.keys():
        status = statuses[service]['status']
        if status == 'scheduled' and global_status < 1:
            global_status = 1
        elif status == 'minor' and global_status < 2:
            global_status = 2
        elif status == 'major' and global_status < 3:
            global_status = 3
    if global_status == 0:
        return 'good'
    elif global_status == 1:
        return 'scheduled'
    elif global_status == 2:
        return 'minor'
    else:
        return 'major'

def generateHtml():
    return generateHtmlPage(getInfo('statuses.json'))

def generateFeed(feedtype):
    return generateFeedPage(feedtype + '.html', getInfo('changes.json'), getInfo('statuses.json'))

def doMinify(original):
    return original.replace("> ",">").replace(" <","<").replace(" >",">").replace("< ","<").replace(" :",":").replace(" ;",";").replace("; ",";").replace("{ ","{").replace(" }","}").replace(" {","{").replace("} ","}").replace("  "," ").replace("\t","")

def minify(contents):
    contents = contents.replace("\n", "")
    prev = contents
    contents = doMinify(contents)
    while prev != contents:
        prev = contents
        contents = doMinify(contents)
    return contents

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate the static files')
    parser.add_argument('type', help='The type of page to generate, either html or rss')
    args = parser.parse_args()

    if args.type == 'html':
       print(minify(generateHtml()))
    elif args.type == 'rss':
       print(minify(generateFeed('rss')))
    else:
        print('Error: invalid type (html/rss)')
        sys.exit(1)
