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

# N人が合宿に参加してD日
# i人目は1日目、Ai+1,2Ai+1にチョコを1個食べた
N = int(input())
D, X = list(map(int, input().split()))
ans = X

for i in range(N):
    a = int(input())
    # １日目の分
    ans += 1
    j = 1
    while (j*a) + 1 <= D:
        ans += 1
        j += 1
print(ans)
