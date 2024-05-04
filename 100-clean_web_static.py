#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py)
"""
from fabric.api import env, run, local
from datetime import datetime
import os

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    try:
        number = int(number)
    except ValueError:
        number = 0

    if number < 1:
        number = 1

    archives_to_keep = sorted(os.listdir("versions"))[-number:]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split("\n")

    for archive in archives:
        if archive not in archives_to_keep:
            run("rm -rf /data/web_static/releases/{}".format(archive))

    local_archives = local("ls -tr versions", capture=True).split("\n")
    for local_archive in local_archives:
        if local_archive not in archives_to_keep:
            local("rm -rf versions/{}".format(local_archive))
