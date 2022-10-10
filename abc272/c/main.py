# -*- coding: utf-8 -*-
"""
異なる2要素の和として表される値の中に偶数が存在するか判定
存在する場合その最大値を求める

偶数になる条件 奇数 + 奇数,偶数+奇数
配列を奇数と偶数に分けてソートすれば最初から最後の要素が答えになる
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N = int(input())
A = list(map(int, input().split()))
evens = []
odds = []

for a in A:
    if a % 2 == 0:
        evens.append(a)
        continue
    odds.append(a)

ans = -1
# 奇数+奇数の場合
if len(odds) > 1:
    tmp = sorted(odds, reverse=True)
    ans = tmp[0] + tmp[1]
# 偶数+偶数の場合
if len(evens) > 1:
    tmp = sorted(evens, reverse=True)
    ans = max(ans, tmp[0] + tmp[1])
print(ans)
