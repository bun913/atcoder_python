# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
A, B, C = list(map(int, input().split()))
mod = 10**9 + 7
ans = A * B % mod
ans = C * ans % mod
print(ans)
