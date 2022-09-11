#!/usr/bin/python3
"""2. Deploy archive!"""
from fabric.api import local, env, run, cd, put
from datetime import datetime
from os.path import isdir
env.use_ssh_config = True
env.hosts = ["54.227.113.133", "184.73.20.152"]
env.user = "ubuntu"


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
    if not archive_path:
        run("echo $HOSTNAME")
        return False
    try:
        file_name = archive_path.split("/")[1]
        name = file_name.replace(".tgz", "")
        path = "/data/web_static/releases/{}".format(name)
        put(archive_path, "/tmp", use_sudo=True)
        run("mkdir -p {}".format(path))
        run("tar xvzf /tmp/{0} -C {1}".format(file_name, path))
        run("rm /tmp/{}".format(file_name))

        with cd("{}/web_static".format(path)):
            run("mv * ../")
        run("rm -rf /data/web_static/current")
        run("ln -sf {} /data/web_static/current".format(path))
        print("New version deployed!")
        return True
    except Exception as err:
        print(err)
        return False
