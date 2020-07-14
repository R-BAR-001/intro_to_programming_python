#!/usr/bin/env python3

from sys import argv

# Using a tuple to store our two variables.
(a, b) = (int(argv[1]), int(argv[2]))

# We are only testing two scenarios in this question, so we use a logical OR.
if (a % b == 0) or (b % a == 0):
    print("True")
else:
    print("False")
