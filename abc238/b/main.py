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

# ピザ(円)自体を回していくとめんどくさい
# なので円は回さずに切り込みをどんどん回していこうということ
# https://youtu.be/Ckuo6w6s_ko?t=1143
# 切り込みの方を動かすので、作っていく切れ込みは反時計回りに回してく
# 各切れ込みを360で割った余りを出していく
# それぞれの差の最大値を出してやれば良い(ただ、0と360を入れておかないと最後のピースの角度が出せない)

N = int(input())
A = list(map(int, input().split()))
P = [0]

for i in range(N):
    p = (P[i] + A[i]) % 360
    P.append(p)
P = sorted(P)
P.append(360)

_max = 0


for i in range(1, len(P)):
    dif = P[i] - P[i-1]
    _max = max(dif, _max)
print(_max)
