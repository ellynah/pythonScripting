#!/usr/bin/python3

import hashlib
import os

# Compute the MD5 digest of a file
def gethash(file):
    hasher = hashlib.md5()
    with open(file, "rb") as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

# Start with an empty dictionary
hashmap = {}

# Recursively visit all files in the directory being scanned
for rootdir, dirs, files in os.walk(".."):
    for f in files:
        path = os.path.join(rootdir, f)
        # Skip short files and symlinks
        if os.path.islink(path) or os.stat(path).st_size < 1024:
            continue
        hash = gethash(path)
        if hash in hashmap:
            matching = hashmap[hash]
            # We have found a pair of identical files
            if os.stat(path).st_ino == os.stat(matching).st_ino:
                print("%s, %s are links to same file" % (path, matching))
                continue
            # Otherwise, delete the new file and link the name to the old one
            else:
                os.unlink(path)
                os.link(matching, path)
                print("%s same as %s" % (path, matching))
        else:
            # Add the hash of the new file to the dictionary
            hashmap[hash] = path

