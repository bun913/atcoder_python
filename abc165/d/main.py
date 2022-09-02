# -*- coding: utf-8 -*-
"""
N以下のx
ただしNが10**12なので一つずつ求めていたら間に合わない
Nをa*bとして表してaを平方根まで数え上げればどうか

以下解説AC
手を動かしてみれば周期性があることに気づく
"""
from math import sqrt

A, B, N = list(map(int, input().split()))


def fl(x: int):
    left = A * x // B
    right = A * (x // B)
    return left - right


ans = fl(min(N, B - 1))
print(ans)
