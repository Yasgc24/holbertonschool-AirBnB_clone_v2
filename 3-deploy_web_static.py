#!/usr/bin/python3
"""3. Full deployment"""
from fabric.api import local, env, run, put
from datetime import datetime
from os.path import isdir, exists
env.hosts = ["54.227.113.133", "184.73.20.152"]


def do_pack():
    """Generates a .tgz archive from the contents"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(date)
    try:
        if isdir("versions") is False:
            local("mkdir versions")
        local("tar -cvzf {} web_static".format(file))
        return file
    except Exception:
        return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not exists(archive_path):
        return False
    try:
        file = archive_path.split('/')[-1].split('.')[0]
        put(archive_path, "/tmp")
        run("mkdir -p /data/web_static/releases/{}/".format(file))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}".format(
            file, file))
        run("rm /tmp/{}.tgz".format(file))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}".format(file, file))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}\
            /data/web_static/current".format(file))
        return True
    except Exception as e:
        return False


def deploy():
    """creates and distributes an archive to your web servers"""
    archive_path = do_pack
    if archive_path:
        do_deploy(archive_path)
    else:
        return False
