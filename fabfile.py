#!/usr/bin/env python2
from fabric.api import env, run

env.use_ssh_config = True


def host_type():
    run('uname -s')
