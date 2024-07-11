#!/usr/bin/python3
"""
Fabric script(based on the file 1-pack_web_static.py) that,
distributes an archive to web servers, using the function do_deploy.
"""
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['54.160.66.54', '34.224.2.3']
env.user = "ubuntu"
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Function that distributes an archive to web servers"""
    if exists(archive_path) is False:
        return False

    try:
        f = archive_path.split('/')[-1]
        f_xt = f.split(".")[0]
        put(archive_path, "/tmp/")
        run(f"mkdir -p /data/web_static/releases/{f_xt}/")
        run(f"tar -xzf /tmp/{f} -C /data/web_static/releases/{f_xt}/")
        run(f"rm /tmp/{f}")
        run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'.format(f_xt, f_xt))
        run(f"rm -rf /data/web_static/releases/{f_xt}/web_static")
        run("rm -rf /data/web_static/current")
        run(
         f"ln -s /data/web_static/releases/{f_xt}/ /data/web_static/current")
        return True
    except:
        return False
