#!/usr/bin/env python3

from sys import argv
from random import randrange
a, b = int(argv[1]), int(argv[2])

# This is strictly between the two inputs.
start = min(a, b) + 1 
stop = max(a, b) 
x = randrange(start, stop)
print(x)
