# -*- coding: utf-8 -*-
"""
解く前のメモ

実はX,pが全て100以下の数字であるので全部数えても間に合う
"""
X, N = list(map(int, input().split()))

if N == 0:
    print(100)
    exit()

P = list(map(int, input().split()))
p_set = set(P)

_min = 101

for i in range(-200, 201):
    if i in p_set:
        continue
    dif = abs(X-i)
    _min = min(_min, dif)

for i in range(-200, 201):
    if i in p_set:
        continue
    dif = abs(X-i)
    if dif == _min:
        print(i)
        exit()
