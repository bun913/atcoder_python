# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
L, R, d = list(map(int, input().split()))
ans = R // d - (L-1) // d
print(ans)
