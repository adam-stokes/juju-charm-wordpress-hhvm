from charms.reactive import (
    hook,
    when,
    only_once,
    is_state
)

import os.path as path
from charmhelpers.core import hookenv, host
from charmhelpers.core.templating import render
from shell import shell

# ./lib/nginxlib
import nginxlib

# ./lib/wordpresslib.py
import wordpresslib

config = hookenv.config()


# HOOKS -----------------------------------------------------------------------
@hook('config-changed')
def config_changed():

    if not is_state('nginx.available'):
        return

    host.service_restart('nginx')
    hookenv.status_set('active', 'Ready')


# REACTORS --------------------------------------------------------------------
@when('nginx.available')
@only_once
def install_app():
    """ Performs application installation
    """

    hookenv.log('Installing Wordpress', 'info')

    # Configure NGINX vhost
    nginxlib.configure_site('default', 'vhost.conf')

    # Update application
    wordpresslib.download_archive()

    host.service_restart('nginx')
    hookenv.status_set('active', 'Wordpress is installed!')

@when('nginx.available', 'database.available')
def setup_mysql(mysql):
    """ mysql available configure wordpress db
    """
    hookenv.status_set('maintenance', 'Wordpress is connecting to MySQL')
    target = os.path.join(nginxlib.get_app_path(), 'wp-config.php.template')
    pass
