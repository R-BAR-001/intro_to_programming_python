#!/usr/bin/env python3

from sys import argv
import datetime

# Compose a program that takes two integers m and d from the cmd line and writes
# true if day d of month m is between 20MAR and 20JUN. 

# https://www.programiz.com/python-programming/datetime/strptime
# https://stackoverflow.com/questions/47545090/how-can-i-check-if-date-is-on-range-on-python

# I'm interpreting the 'between' with <= / >=. Additionally, this program can't
# handle incorrect dates.

(m, d) = (str(argv[1]), str(argv[2]))

input = datetime.datetime.strptime(m + "/" + d, "%m/%d")
start = datetime.datetime.strptime("3/20", "%m/%d")
end = datetime.datetime.strptime("6/20", "%m/%d")

if start <= input <= end:
    print("True")
else:
    print("False")
