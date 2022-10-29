# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
a, b, c, d, e, f = list(map(int, input().split()))
mod = 998244353
left = a % mod * b % mod * c % mod
right = d % mod * e % mod * f % mod
ans = (left - right) % mod
print(ans)
