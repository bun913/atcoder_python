# -*- coding: utf-8 -*-
"""
2019年なのでうるう年は関係ない
M1月D1日が月末か求める
M2月D2日であることがわかっている
どうもこうも、別にきにせずにD2が1か判定すれば良くね
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

m1, d1 = list(map(int, input().split()))
m2, d2 = list(map(int, input().split()))

if d2 == 1:
    print(1)
    exit()
print(0)
