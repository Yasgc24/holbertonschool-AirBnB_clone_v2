#!/usr/bin/python3
"""4. Keep it clean!"""
from fabric.api import local, env, run, cd, put, lcd
env.use_ssh_config = True
env.hosts = ["54.227.113.133", "184.73.20.152"]
env.user = "ubuntu"


def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number in [0, 1]:
        number = 2
    else:
        number += 1
    with lcd("./versions"):
        local("rm -rf $(ls -t | grep web_static | tail -n+{}".format(number))
    with cd("/data/web_static/releases"):
        run("rm -rf $(ls -t | grep web_static | tail -n+{}".format(number))
