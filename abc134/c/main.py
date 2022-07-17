# -*- coding: utf-8 -*-
"""
解く前のメモ

自分意外の要素で最大のものを出力せよということ
てことは、大きい順にメモをしておいて、基本的に最大のものを出力する
でも、もし自分が最大のものだったら次の要素をみるっていうだけの話では
"""
# 数列中のAiを除くN-1個の要素のうちの最大値
N = int(input())
A = [int(input()) for _ in range(N)]
_sorted = sorted(A, reverse=True)
_max = _sorted[0]

for i in range(N):
    ans = _max
    if A[i] == _max:
        ans = _sorted[1]
    print(ans)
