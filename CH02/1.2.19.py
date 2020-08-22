#!/usr/bin/env python3

from sys import argv

G = 9.80665
x, v, t = float(argv[1]), float(argv[2]), float(argv[3])
output = x + v*t - .5*G*(t**2)
print(output)

