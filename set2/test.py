# !/usr/bin/python
# coding:UTF-8
# 2-(16)
"""
import sys

argv = sys.argv
argc = len(argv)

if argc != 2:
    print "Error!"

n = int(sys.argv[1])

f = open("hightemp.txt", "r")
lst = []
sub = []

num = 24 / n

print num
for line in f.readlines():
    lst.append(line)

for i in lst:
    sub.append(i)
    if len(sub) == num:
        for j in sub:
            print j,
        print "\n".strip()
        del sub[:]
#print zip(*[iter(lst)]*3)
"""

import sys

f = open("hightemp.txt", "r")
lst = []
sub1 = []
sub2 = []

num = 4

for line in f.readlines():
    sub1.append(line)
    if len(sub1) == num:
        sub2.append(sub1[0])
        print sub2
#    del sub1[:]

#print sub2
