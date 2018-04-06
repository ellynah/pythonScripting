# pythonScripting
Python Quick Start for Linux System Administrators

## Python Quick Start

```python
#!/usr/bin/python3

def factorial(n):
    fac = 1
    for x in range(1, n + 1):
        fac = fac * x
    return fac

print(factorial(5))
```

![1_1_comparing.png](https://github.com/ellynah/pythonScripting/blob/master/screen_shot/1_1_comparing.png)



```python
#!/usr/bin/python3

import os.path

if os.path.exists("/etc/hosts"):
    print("hosts file exists")
else:
    print("no hosts file")
```

![1_2_comparing.png](https://github.com/ellynah/pythonScripting/blob/master/screen_shot/1_2_comparing.png)


```python
#!/usr/bin/python3

try:
    f = open("/etc/hosts")
    print("file exist")
except FileNotFoundError:
    print("no hosts file")
```

![1_3_pythonic_way.png](https://github.com/ellynah/pythonScripting/blob/master/screen_shot/1_3_pythonic_way.png)


```python
#!/usr/bin/python3

maxuid = 0
for line in open("/etc/passwd"):
    split = line.split(":")
    maxuid = max(maxuid, int(split[2]))

print(maxuid)
```

![1_4_find_uid.png](https://github.com/ellynah/pythonScripting/blob/master/screen_shot/1_4_find_uid.png)

```python
import tarfile
import glob


def create_tarfile():
    tfile = tarfile.open("mytarfile.tar", "w")
    for config_file in glob.glob("~"):
        tfile.add(config_file)
    tfile.close()


create_tarfile()
```

![2_1_tarfile.png](https://github.com/ellynah/pythonScripting/blob/master/screen_shot/2_1_tarfile.png)

```python
#!/usr/bin/python3

import os

for file in os.listdir("."):
    info = os.stat(file)
    print("%-20s : size %d" % (file, info.st_size))
```

![3_1_listdir.png](https://github.com/ellynah/pythonScripting/blob/master/screen_shot/3_1_listdir.png)

```python
#!/usr/bin/python3

import os

for dirpath, dirnames, filenames in os.walk("."):
    print("Files in %s are:" % dirpath)
    for file in filenames:
        print("\t" + file)
    print("Directories in %s are:" % dirpath)
    for dir in dirnames:
        print("\t" + dir)
```

![3_2_listdir.png](https://github.com/ellynah/pythonScripting/blob/master/screen_shot/3_2_listdir.png)

```python
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


```

![3_3_deduplicate.png](https://github.com/ellynah/pythonScripting/blob/master/screen_shot/3_3_deduplicate.png)

```python
#!/usr/bin/python3

# Playing with file descriptors

import sys

print("this is written to stdout")

print("this is written to stderr", file = sys.stderr)

# Write to a text file
f = open("out1", "w")
print("this is written to out1", file = f)
f.close()

# More pythonic way
with open("out2", "w") as f:
    print("this is written to out2", file = f)

# Temporarily redirecting stdout
old_stdout = sys.stdout
with open("out3", "w") as f:
    sys.stdout = f
    print("this is written to out3")
sys.stdout = old_stdout
print("stdout is restored")
```

![4_1_streams.png](https://github.com/ellynah/pythonScripting/blob/master/screen_shot/4_1_streams.png)


```python
#!/usr/bin/python3

# optparse demo -- option parsing for our "df" wrapper

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", "--threshold",
                  dest="threshold",
                  type="int",
                  default=90,
                  help="Set threshold (%)")
parser.add_option("-s", "--single",
                  action="store_true",
                  dest="singleshot",
                  default=False,
                  help="just check once, don't loop")
parser.add_option("-m", "--mailbox",
                  dest="mailbox",
                  help="mail report to this mailbox")

# For now, just print out our options and arguments
(options, args) = parser.parse_args()
print("singleshot is %r" % options.singleshot)
print("mailbox is %s" % options.mailbox)
print("threshold is %d" % options.threshold)
print("non-option argument list is %s" % str(args))
```

![4_2_parse.png](https://github.com/ellynah/pythonScripting/blob/master/screen_shot/4_2_parse.png)


```python
#!/usr/bin/python3

# Program to find prime numbers.
# Intended for demonstrating signals

from time import sleep
from signal import *

def isprime(n):
    sleep(0.1)
    x = 2
    while (x * x ) <= n:
        if not n % x:
            return False
        x += 1
    return True

# SIGHUP turns debug printing on and off
debug = False   
def sighup_handler(signum, frame):
    global debug    # Otherwise would be assumed local
    debug = not debug

signal(SIGHUP, sighup_handler)

# SIGUSR1 reports current status
def report_status(signum, frame):
    global primes_list
    print("found %d primes so far" % len(primes_list))

signal(SIGUSR1, report_status)

# Some other signals are ignored
signal(SIGINT, SIG_IGN)
signal(SIGQUIT, SIG_IGN)
signal(SIGTERM, SIG_IGN)

n = 1
primes_list = []

while True:
    if isprime(n):
        if debug:
            print("%d is prime" % n)
        primes_list.append(n)
    n += 1
```

![4_3_is_prime.png](https://github.com/ellynah/pythonScripting/blob/master/screen_shot/4_3_is_prime.png)




