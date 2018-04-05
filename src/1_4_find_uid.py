#!/usr/bin/python3

maxuid = 0
for line in open("/etc/passwd"):
    split = line.split(":")
    maxuid = max(maxuid, int(split[2]))

print(maxuid)