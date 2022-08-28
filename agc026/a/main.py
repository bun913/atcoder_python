# -*- coding: utf-8 -*-
"""
同じ色は合体してしまう
魔法でスライムの色を変えられる
何回魔法を唱える必要があるか

groupbyで2以上担っているとこを数え上げればよいだけ
"""
from itertools import groupby

N = int(input())
A = list(map(int, input().split()))

grouped = [(k, len(list(g))) for k, g in groupby(A)]
ans = 0

for k, length in grouped:
    if length >= 2:
        ans += length // 2
print(ans)
