# -*- coding: utf-8 -*-
"""
解く前のメモ

今回はA~Eしかないのがわかっているため、全ての並び替えのパターンを試して間に合う
"""
from itertools import permutations

X = [int(input()) for _ in range(5)]
# 順列を取得
perm = list(permutations(X))

ans = 100000 * 5

for x in perm:
    _sum = 0
    for i in range(5):
        a = x[i]
        t = a
        # 最後の注文の場合は10の倍数の考慮不要
        if i == 4:
            _sum += t
            continue
        # それ以外の場合10の倍数を考慮
        if t % 10 == 0:
            _sum += t
            continue
        rest = t % 10
        _sum += t + (10 - rest)
    ans = min(ans, _sum)
print(ans)
