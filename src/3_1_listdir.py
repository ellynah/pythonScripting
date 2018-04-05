#!/usr/bin/python3

import os

for file in os.listdir("."):
    info = os.stat(file)
    print("%-20s : size %d" % (file, info.st_size))