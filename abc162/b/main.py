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
from decimal import Decimal

N = int(input())
ans = Decimal('0')
i = 1

while i < N+1:
    if i % 15 == 0 or i % 5 == 0 or i % 3 == 0:
        i += 1
        continue
    ans += Decimal(str(i))
    i += 1
print(ans)
