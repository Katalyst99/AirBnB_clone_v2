#!/usr/bin/python3
"""
Fabric script(based on the file 2-do_deploy_web_static.py) that creates,
and distributes an archive to web servers, using the function deploy.
"""
from datetime import datetime
from fabric.api import *
import os

env.hosts = ['54.160.66.54', '34.224.2.3']


def do_pack():
    """
    Function that generates a .tgz archive from the contents of,
    the web_static folder.
    """
    current_dt = datetime.now()
    dt_form = "%Y%m%d%H%M%S"
    dt = current_dt.strftime(dt_form)
    if not os.path.exists('versions'):
        local('mkdir -p versions')
    f = "versions/web_static_{}.tgz".format(dt)
    output = local('tar -cvzf {} web_static'.format(f))
    if output.failed:
        return None
    else:
        return f


def do_deploy(archive_path):
    """Function that distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    f = archive_path.split('/')[-1]
    f_xt = f.split(".")[0]
    try:
        dest = '/data/web_static/releases/'
        put(archive_path, "/tmp/")
        run(f"mkdir -p {dest}{f_xt}/")
        run(f"tar -xzf /tmp/{f} -C {dest}{f_xt}/")
        run(f"rm /tmp/{f}")
        run('mv {0}{1}/web_static/* {0}{1}/'.format(dest, f_xt))
        run(f"rm -rf {dest}{f_xt}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {dest}{f_xt}/ /data/web_static/current")
        return True
    except:
        return False


def deploy():
    """Function that creates and distributes an archive to web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
