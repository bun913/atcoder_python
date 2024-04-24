# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from math import sqrt

setrecursionlimit(10**8)

N = int(input())
# 1以上9以下のNの約数を先に列挙しておく
dv = []
for i in range(1, 10):
    if N % i == 0:
        dv.append(i)

ans_list = []
for i in range(N+1):
    i_ans = "-"
    for j in dv:
        r = N // j
        if i % r == 0:
            i_ans = str(j)
            break
    ans_list.append(i_ans)
print("".join(ans_list))
