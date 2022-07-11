# -*- coding: utf-8 -*-
from itertools import permutations
from math import sqrt
from statistics import mean

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]
# Nがたかだか8なので順列の全列挙でなんとかなりそう
t = [i for i in range(N)]
orders = list(permutations(t))
dists = []

for order in orders:
    dist = 0
    for j in range(1, N):
        bef = order[j-1]
        cur = order[j]
        curx = XY[cur][0]
        cury = XY[cur][1]
        befx = XY[bef][0]
        befy = XY[bef][1]
        d = sqrt((curx-befx) ** 2 + (cury - befy) ** 2)
        dist += d
    dists.append(dist)

ans = mean(dists)
print(ans)
