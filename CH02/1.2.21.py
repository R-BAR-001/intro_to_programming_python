#!/usr/bin/env python3

# Compound interest- implementing Pe^(rt) formula.

import math
p  = float(input("[P]rinciple: "))
r = float(input("[R]ate of interest: "))/100
t = float(input("[T]ime in years: "))

a = p * pow(math.e, (r*t))
print(a)

