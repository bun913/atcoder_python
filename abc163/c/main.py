# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from functools import reduce
from itertools import combinations
import math

# N人の社員がいる
# 社員番号が1の人がルート(上司がいない)
# 自分より社員番号が小さい直属の上司が一人だけいる
# 親が一つの木構造と言える
# 社員番号iの直属の上司の社員番号がAiで与えられる
# 各社員について直属の社員が何人いるか求めること
# 直属だけであることに注意
# 単純に出現回数じゃね

N = int(input())
A = list(map(int, input().split()))
dic = dict([(i, 0) for i in range(1, N+1)])

for a in A:
    dic[a] += 1
for i in range(1, N+1):
    print(dic[i])
