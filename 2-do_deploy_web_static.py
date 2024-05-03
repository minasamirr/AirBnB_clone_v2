#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from fabric.api import run, put, env
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to
        # /data/web_static/releases/<archive filename without extension>
        file_name = archive_path.split('/')[-1]
        folder_name = file_name.split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(file_name, folder_name))

        # Remove the archive from the web server
        run('rm /tmp/{}'.format(file_name))

        # Move contents of extracted folder to main directory
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'
            .format(folder_name, folder_name))

        # Remove the extracted folder
        run('rm -rf /data/web_static/releases/{}/web_static'.format(folder_name))

        # Delete the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link linked to the new version of the code
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(folder_name))

        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False
