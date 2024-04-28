# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)

N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

for n in range(0, 101):
    # 最後のスコアを全探索で求める
    # 1つでもN以上のスコアを作れるならそのスコアを出力する
    l = [n] + A
    sorted_l = sorted(l)
    sorted_l[0] = 0
    sorted_l[-1] = 0
    total = sum(sorted_l)
    if total >= X:
        print(n)
        exit()
print(-1)
