# -*- coding: utf-8 -*-
"""
解く前のメモ

価値のあるやつを最後に残した方が良さそう
基本的に価値の低いものからpopして合成すればよさそう

毎回sortしないといけないわけだが、sort自体がlognの計算でできるはずなので間に合うはず
"""

N = int(input())
V = list(map(int, input().split()))

_sorted = sorted(V)
while not len(_sorted) == 1:
    a = _sorted.pop(0)
    b = _sorted.pop(0)
    c = (a+b) / 2
    _sorted = sorted(_sorted + [c])
print(_sorted[0])
