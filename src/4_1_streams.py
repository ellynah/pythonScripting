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




