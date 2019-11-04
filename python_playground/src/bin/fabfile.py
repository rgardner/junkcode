#!/usr/bin/env python3

from fabric import Connection


def host_type(conn: Connection):
    conn.run("uname -s")
