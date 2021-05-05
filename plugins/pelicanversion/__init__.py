from pelican import signals
import pelican as p
from packaging import version

def check_version(pelican):
    if version.parse(pelican.settings['MIN_PELICAN_VERSION']) > version.parse(p.__version__):
        raise Exception(f"We Require Pelican v{pelican.settings['MIN_PELICAN_VERSION']} -- found v{p.__version__}" )

def register():
    """Plugin registration."""
    signals.generator_init.connect(check_version)