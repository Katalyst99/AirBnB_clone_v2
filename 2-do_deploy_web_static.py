#!/usr/bin/python3
"""
Fabric script(based on the file 1-pack_web_static.py) that,
distributes an archive to web servers, using the function do_deploy.
"""
from fabric.api import *
import os

env.hosts = ['54.160.66.54', '34.224.2.3']
env.user = "ubuntu"
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Function that distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    f = archive_path.split('/')[-1]
    f_xt = f.split(".")[0]
    try:
        put(archive_path, "/tmp/")
        run(f"mkdir -p /data/web_static/releases/{f_xt}")
        run(f"tar -xzf /tmp/{f} -C /data/web_static/releases/{f_xt}")
        run(f"rm /tmp/{f}")
        run(f"mv /data/web_static/releases/{f_xt}/web_static/* \
            /data/web_static/releases/{f_xt}")
        run(f"rm -rf /data/web_static/releases/{f_xt}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{f_xt} /data/web_static/current")
        return True
    except Exception:
        return False
