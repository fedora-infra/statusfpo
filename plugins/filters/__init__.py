from pelican import signals

from . import filters

def add_filters(pelican):
    """register filters to Pelican."""
    pelican.env.filters.update({"parsedate": filters.parsedate})
    pelican.env.filters.update({"formatdate": filters.formatdate})
    pelican.env.filters.update({"categories_dict": filters.categories_dict})

def register():
    """Plugin registration."""
    signals.generator_init.connect(add_filters)