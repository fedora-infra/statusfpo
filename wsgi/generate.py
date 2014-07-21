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

from util_functions import *

def getInfo(filename):
    f = open(filename, 'r')
    info = json.loads(f.read())
    f.close()
    return info

def get_update_title(change):
    if not 'new_global_status' in change.keys():
        return 'Service change'
    else:
        return getVerboseStatus(change['new_global_status'])

def generateFeedPage(feedtype, changes, statuses):
    env = Environment(loader=FileSystemLoader('.'))
    newchanges = []
    for change in changes:
        change['update_title'] = get_update_title(change)
        change['datetime'] = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(change['changedate']))
        newchanges.append(change)
        if change['changetype'] == 'single':
            change['serviceName'] = statuses['services'][change['service']]['name']
        else:
            change['serviceNames'] = []
            for srv in change['services']:
                change['serviceNames'].append(statuses['services'][srv]['name'])
    global_status = getVerboseStatus(getGlobalStatus(statuses['services']))
    return env.get_template(feedtype).render(changes=changes, currenttime=strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))

def generateHtmlPage(statuses):
    env = Environment(loader=FileSystemLoader('.'))
    global_status = getVerboseStatus(getGlobalStatus(statuses['services']))
    return env.get_template('template.html').render(statuses=statuses['services'], global_status=getGlobalStatus(statuses['services']), global_info=statuses['global_info'], verbose_global_status=global_status, year=datetime.datetime.now().year)

def generateMobilePage(statuses):
    env = Environment(loader=FileSystemLoader('.'))
    global_status = getVerboseStatus(getGlobalStatus(statuses['services']))
    failed_services = getFailedServices(statuses['services'])
    return env.get_template('mobile.html').render(statuses=statuses['services'], global_status=getGlobalStatus(statuses['services']), global_info=statuses['global_info'], verbose_global_status=global_status, failed_services=failed_services, year=datetime.datetime.now().year)

def getFailedServices(statuses):
    toReturn = []
    for service in statuses.keys():
        if statuses[service]['status'] != 'good':
            toReturn.append(statuses[service]['name'] + ' (' + statuses[service]['status'] + ')')
    return ', '.join(toReturn)

def generateHtml():
    return generateHtmlPage(getInfo('statuses.json'))

def generateFeed(feedtype):
    return generateFeedPage(feedtype + '.html', getInfo('changes.json'), getInfo('statuses.json'))

def generateMobile():
    return generateMobilePage(getInfo('statuses.json'))

def doMinify(original):
    return original.replace(" >",">").replace("< ","<").replace(" :",":").replace(" ;",";").replace("; ",";").replace("{ ","{").replace(" }","}").replace(" {","{").replace("} ","}").replace("  "," ").replace("\t","")

def minify(contents, skip):
    if skip:
        return contents
    contents = contents.replace("\n", "")
    prev = contents
    contents = doMinify(contents)
    while prev != contents:
        prev = contents
        contents = doMinify(contents)
    return contents

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate the static files')
    parser.add_argument('type', help='The type of page to generate, either html, mobile or rss')
    parser.add_argument('--no-minify', action='store_true', help='Disable the minification, to ease debugging')
    args = parser.parse_args()

    the_json = getInfo('statuses.json')
    the_json['global_verbose_status'] = getVerboseStatus(getGlobalStatus(the_json['services']))
    the_json['global_status'] = getGlobalStatus(the_json['services'])

    f = open('statuses.json', 'w')
    f.write(json.dumps(the_json, sort_keys=True, indent = 4))
    f.close()

    if args.type == 'html':
        print(minify(generateHtml(), args.no_minify))
    elif args.type == 'rss':
        print(minify(generateFeed('rss'), args.no_minify))
    elif args.type == 'mobile':
        print(minify(generateMobile(), args.no_minify))
    else:
        print('Error: invalid type (html/rss)')
        sys.exit(1)
