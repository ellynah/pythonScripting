#!/usr/bin/python3

try:
    f = open("/etc/hosts")
    print("file exist")
except FileNotFoundError:
    print("no hosts file")