# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
N = int(input())


def f(a, b):
    return max(len(str(a)), len(str(b)))


# 約数の列挙をlogNまでしていく
limit = int(N**0.5) + 1
ans = float("inf")
for a in range(1, limit):
    if N % a == 0:
        b = N // a
        ans = min(ans, f(a, b))
print(ans)
