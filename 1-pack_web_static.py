#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive,
from the contents of the web_static folder of  AirBnB Clone repo,
using the function do_pack.
"""
from datetime import datetime
from fabric.api import local
import os


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
