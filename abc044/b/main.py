# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from collections import Counter

W = input()
c = Counter(W)
for p in c.most_common():
    if p[1] % 2 != 0:
        print("No")
        exit()
print("Yes")
