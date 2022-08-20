# -*- coding: utf-8 -*-
"""
解く前のメモ

ABがそもそも非常に大きい
gcdをlogで求めることは必須
ユークリッドの互助法かな

ただ最小公倍数を求める時にAとBをかけるととんでもない数になる
"""
from math import gcd

A, B = list(map(int, input().split()))
g = gcd(A, B)
lcm = A//g*B
if lcm > 10 ** 18:
    print('Large')
    exit()
print(lcm)
