#!/usr/bin/env python3

from sys import argv

a, b, c, = int(argv[1]), int(argv[2]), int(argv[3])

if (a >= b + c) or (b >= a + c) or (c >= b + a):
    print("False")
else:
    print("True")

