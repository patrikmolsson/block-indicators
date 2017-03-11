#!/usr/bin/env python3
import re
from subprocess import check_output

out = check_output(["amixer", "get", "'Master'"]).decode('UTF-8')

power = re.search('off', out);

p = "<span font='FontAwesome'>{}</span>{}"

if power is not None:
    print(p.format("\uf026", ""))
else:
    volume = re.search('\d+%', out)
    print(p.format("\uf028", " " + volume.group(0)))
