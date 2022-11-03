# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
W, a, b = list(map(int, input().split()))
a_end = a + W
b_start = b
b_end = b + W
# bが右に離れている
if b_start >= a_end:
    print(b_start - a_end)
elif a >= b_end:
    print(a - b_end)
else:
    print(0)
