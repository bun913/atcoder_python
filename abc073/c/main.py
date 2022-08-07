# -*- coding: utf-8 -*-
"""
解く前のメモ

言われた時点での数を表すsetを用意して、あれば書く、なければ消すを繰り返すだけでは
"""

N = int(input())
s = set()

for i in range(N):
    a = int(input())
    if a in s:
        s.remove(a)
        continue
    s.add(a)
print(len(s))
