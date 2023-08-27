# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from math import ceil

A, B = map(int, input().split())
div = A // B
if A % B != 0:
    div += 1
print(div)
