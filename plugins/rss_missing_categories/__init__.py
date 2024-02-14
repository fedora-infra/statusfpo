"""Ensure RSS feeds for all “well-known” categories are published."""

from pelican import generators, signals


class RSSMissingCategoriesGenerator(generators.ArticlesGenerator):
    def generate_feeds(self, writer):
        missing = {"ongoing", "planned", "resolved"} - {
            cat.name for cat, art in self.categories
        }

        for cat in missing:
            writer.write_feed(
                [],  # articles
                self.context,
                path=f"{cat}.rss",
                feed_title=cat,
                feed_type="rss",
            )

    def generate_output(self, writer):
        self.generate_feeds(writer)


def get_generators(pelican_object):
    return RSSMissingCategoriesGenerator


def register():
    signals.get_generators.connect(get_generators)
