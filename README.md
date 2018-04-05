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
