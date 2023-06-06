# -*- coding: utf-8 -*-
"""
f(n)を以下の2つの条件の両方を満たすような3つの整数の組みx,y,y
- 1 <= x,y,z
- x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x = n
整数Nが与えられるので、f(1) + f(2) + ... + f(N)を求めてください。
Nがたかだか10**4なので、10,000ですよ。
だからx**2とする時点で実は高々100まで調べれば十分
"""
N = int(input())
ans = [0 for _ in range(N)]
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            total = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            if total <= N:
                ans[total - 1] += 1
for i in range(N):
    print(ans[i])
