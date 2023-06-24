# -*- coding: utf-8 -*-
"""
AとBの最小公倍数を求める
"""
from math import gcd
A, B = map(int, input().split())
gc = gcd(A, B)
lcm = A * B // gc
print(lcm)
