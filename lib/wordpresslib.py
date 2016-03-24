import sys
from os import path, makedirs
from shutil import rmtree
from charmhelpers.core import hookenv
from hashlib import sha256
from shell import shell

from nginxlib import get_app_path


def download_archive():
    """
    """
    # Get the nginx vhost application path
    app_path = get_app_path()

    config = hookenv.config()
    shell('rm /tmp/wordpress.tgz || true')
    cmd = ('wget -q -O /tmp/wordpress.tgz '
           'http://wordpress.org/latest.tar.gz')
    hookenv.log("Downloading Wordpress: {}".format(cmd))
    shell(cmd)

    with open('/tmp/wordpress.tgz', 'rb') as fp:
        dl_byte = sha256(fp.read())
        if dl_byte.hexdigest() != config['checksum']:
            hookenv.status_set(
                'blocked',
                'Downloaded Wordpress checksums do not match, '
                'possibly because of a new stable release. '
                'Check wordpress.org!')
            sys.exit(0)

    if path.isdir(app_path):
        rmtree(app_path)
    makedirs(app_path)

    cmd = ('tar -xf /tmp/wordpress.tgz --strip-components=1 -C {}'.format(
        app_path
    ))
    hookenv.log("Extracting Wordpress: {}".format(cmd))
    shell(cmd)
