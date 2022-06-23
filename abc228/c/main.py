# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

1行1列データ

#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())
#float型　(小数)で受け取るとき
s = float(input())

(1,N)行列データ
s = input().split()
# listで整数で受け取る
l = list(map(int, input().split()))

その他
https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))
"""
from functools import reduce
from itertools import combinations
import itertools
import math

N, K = list(map(int, input().split()))
P = []
scores = []
for _ in range(N):
    l = list(map(int, input().split()))
    scores.append(sum(l))
    P.append(l)
scores = sorted(scores, reverse=True)
for i in range(N):
    now = sum(P[i])
    if now + 300 >= scores[K-1]:
        print('Yes')
        continue
    print('No')
