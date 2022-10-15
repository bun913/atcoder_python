# -*- coding: utf-8 -*-
"""
解く前のメモ用
自分より大きいものの数を求める
あらかじめ自分が何番目かわかっておけば良いのでは
# K = i-1の場合の問題の答えを出力する
"""
from bisect import bisect_right
from collections import defaultdict, Counter

N = int(input())
A = list(map(int, input().split()))
B = sorted(set(A))
c = Counter(A)

# 自分より大きいものの数をあらかじめメモしておく
memo = defaultdict(int)
for a in A:
    ind = bisect_right(B, a)
    o = len(B) - ind
    memo[o] = c[a]

for k, a in enumerate(A):
    print(memo[k])
