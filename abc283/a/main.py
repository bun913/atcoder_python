# -*- coding: utf-8 -*-
"""
Qが10**5でリスト操作はO(1)なので余裕
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

A, B = list(map(int, input().split()))
print(A**B)
