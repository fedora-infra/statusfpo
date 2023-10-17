"""
Fedora Status outage json generator
"""

import json
from pelican import signals, generators, writers, urlwrappers


class FeedClass(object):
    def __init__(self, title):
        self.feed = {"outages": []}

    def add_item(self, item):
        self.feed["outages"].append(item)

    def write(self, outfile, encoding):
        json.dump(self.feed, outfile)


class JSONGenerator(generators.ArticlesGenerator):
    def generate_feeds(self, writer):
        missing = set(["ongoing", "planned", "resolved"]) - set(
            [cat.name for cat, art in self.categories]
        )
        for c in missing:
            self.categories.append((urlwrappers.Category(c, {}), []))

        for category, articles in self.categories:
            articles.sort(key=lambda d: d.date, reverse=True)
            writer.write_feed(
                articles,
                self.context,
                path=f"{category.name}.json",
                feed_title=category.name,
                feed_type="json",
            )

    def generate_output(self, writer):
        self.generate_feeds(writer)


class JSONWriter(writers.Writer, object):
    def _create_new_feed(self, feed_type, feed_title, context):
        feed = FeedClass(title=feed_title)
        return feed

    def _add_item_to_the_feed(self, feed, item):
        timeformat = "%Y-%m-%dT%H:%M:%S%z"
        enddate = item.metadata.get("OutageFinish")
        startdate = item.metadata.get("date")
        if enddate:
            enddate = enddate.strftime(timeformat)
        if startdate:
            startdate = startdate.strftime(timeformat)
        feed.add_item(
            {
                "title": item.metadata.get("title"),
                "ticket": {"id": item.metadata.get("ticket"), "url":f"https://pagure.io/fedora-infrastructure/issue/{item.metadata.get('ticket')}"},
                "startdate": startdate,
                "enddate": enddate,
            }
        )


def get_generators(generators):
    return JSONGenerator


def get_writer(writer):
    return JSONWriter


def register():
    signals.get_writer.connect(get_writer)
    signals.get_generators.connect(get_generators)
