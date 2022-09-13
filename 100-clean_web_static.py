#!/usr/bin/python3
"""4. Keep it clean!"""
from fabric.api import *
from datetime import datetime
env.hosts = ['154.227.113.133', '184.73.20.152']


def do_clean(number=0):
    """ Removes all but given number of archives"""
    number = int(number)
    if number < 2:
        number = 1
    number += 1
    number = str(number)
    with lcd("versions"):
        local("ls -1t | grep web_static_.*\.tgz | tail -n +" +
              number + " | xargs -I {} rm -- {}")
    with cd("/data/web_static/releases"):
        run("ls -1t | grep web_static_ | tail -n +" +
            number + " | xargs -I {} rm -rf -- {}")
