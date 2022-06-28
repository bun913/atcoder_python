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

# 公式解説Youtubeで教えてもらった解法
# 2Kまで回ることで各区間の距離を求めることができる
# それにより一番長い区間を回らない経路を取れば良いと言う方法
# (今回の場合2kまでしなくても、最後の点から最初の点までの距離だけ求めればよい)
l = A + [A[0]]
longest = -1

for i in range(1, N+1):
    dis = l[i] - l[i-1]
    if dis < 0:
        dis += K
    longest = max(longest, dis)
print(K-longest)
