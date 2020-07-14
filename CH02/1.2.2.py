#!/usr/bin/env python3

# Importing multiple parts of a single library here
from math import sin, cos
from sys import argv

theta = float(argv[1])
x = sin(theta)**2 + cos(theta)**2
print(x)

