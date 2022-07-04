# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from functools import reduce, lru_cache
from itertools import combinations
import math

N = int(input())
A = list(map(int, input().split()))
# それぞれの足元に0以上の踏み台を設置
# 全ての人が、踏み台を込めて身長を比較した時、自分より前に自分より背の高い人が存在しない
# 基本的に前の人との差分をとっていくわけだが、それまでに見つけた最大値と高い方を比べないといけない
ans = 0
_max = A[0]
for i in range(1, N):
    cur = A[i]
    if _max > cur:
        ans += _max - cur
    _max = max(cur, _max)
print(ans)
