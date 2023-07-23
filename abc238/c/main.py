# -*- coding: utf-8 -*-
"""
"""


def sum_to(a, b):
    return (b-a+1) * (a+b) // 2


N = int(input())
mod = 998244353
dig = len(str(N))
# 一つ前の桁までを等差数列の和の公式で求める
ans = 0
for e in range(1, dig):
    # aが初項
    a = 1
    # bが末項
    b = 9 * 10**(e-1)
    cnt = sum_to(a, b)
    ans += cnt
    ans %= mod
# Nと同じ桁数の数を求める
a = 1  # 初項
b = N-10**(dig-1) + 1  # 末項
cnt = sum_to(a, b)
ans += cnt
ans %= mod
print(ans)
