#!/usr/bin/env python3

from sys import argv
from math import sin

t = float(argv[1])

x = sin(2 * t) + sin(3 * t)

print(x)

