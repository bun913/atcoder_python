# -*- coding: utf-8 -*-
"""
SがAから始まる26進数と考えると計算できる
Sの長さは高々16桁とわかっている
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)


def alpha2num(alpha):
    num = 0
    for index, item in enumerate(list(alpha)):
        num += pow(26, len(alpha)-index-1)*(ord(item)-ord('A')+1)
    return num


S = input()
e = 0
ans = 0
for s in S[::-1]:
    # アルファベットを数字に変換する
    n = alpha2num(s)
    ans += n * (26 ** e)
    e += 1
print(ans)
