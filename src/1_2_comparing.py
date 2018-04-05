#!/usr/bin/python3

import os.path

if os.path.exists("/etc/hosts"):
    print("hosts file exists")
else:
    print("no hosts file")