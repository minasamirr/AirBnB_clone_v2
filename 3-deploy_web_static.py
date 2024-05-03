#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers
"""

from fabric.api import local, env
from os.path import exists
from datetime import datetime
from fabric.operations import put, run
from fabric.context_managers import cd

env.hosts = ['100.25.179.159', '54.145.241.80']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(timestamp)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/<archive filename without extension>
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


def deploy():
    """
    Creates and distributes an archive to the web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

