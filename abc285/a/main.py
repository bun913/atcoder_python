# -*- coding: utf-8 -*-
"""
解く前のメモ用
直接つながっている数字は2*a or 2*a + 1
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)
a, b = list(map(int, input().split()))
if 2 * a == b or 2 * a + 1 == b:
    print("Yes")
    exit()
print("No")
