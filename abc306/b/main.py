# -*- coding: utf-8 -*-
"""
解く前のメモ用
普通に10進数に帰れば良さそう
"""
A = list(map(str, input().split()))
RA = A[::-1]
s = "".join(RA)
ans = int(s, 2)
print(ans)
