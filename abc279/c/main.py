# -*- coding: utf-8 -*-
"""
Sの列を並び替えて、Tと同じにできるかを調べる
H * W <= 4 * 10**5
普通に考えれば書く列を文字列として変換
その文字列の出現回数が一致すればOKかな？
"""
from sys import setrecursionlimit
from collections import Counter

setrecursionlimit(10**7)

H, W = list(map(int, input().split()))
S = [list(input()) for _ in range(H)]
T = [list(input()) for _ in range(H)]

sz = zip(*S)
tz = zip(*T)

s = ["".join(r) for r in sz]
t = ["".join(r) for r in tz]

cs = Counter(s)
ct = Counter(t)

for k, v in cs.items():
    if v != ct[k]:
        print("No")
        exit()
print("Yes")
