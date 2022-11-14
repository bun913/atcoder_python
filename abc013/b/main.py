# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
a = int(input())
b = int(input())
cand1 = abs(b - a)
cand2 = a + (9 - b) + 1
cand3 = (9 - a) + b + 1
print(min([cand1, cand2, cand3]))
