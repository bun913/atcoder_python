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

K, N = list(map(int, input().split()))
A = list(map(int, input().split()))

# この手の問題を円環の問題と言うらしい
# 円環の問題は一直線の数直線で表すことができれば楽
# 例えば点間の距離だとKを２枚することで、最後の点から最初の点の距離とかも扱いやすくなる

# 今回で言えば点の最小距離は普通にどこかの点から時計回りに回って得られる

# 単純に最後の点から最初の点までの距離を求めておく
ans = abs(A[0] - A[N-1])

# あとはiからスタート地点までの距離、スタート地点からiまでの距離を合算しておけば良い
for i in range(N):
    i_to_start = K - A[i]
    start_to_i = A[i-1]
    ans = min(ans, i_to_start + start_to_i)
print(ans)
