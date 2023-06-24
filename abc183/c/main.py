# -*- coding: utf-8 -*-
"""
メタ的な読みとなるがNが8の段階で全探索だなと気づく
これは全ての並び替えのパターンを持っておけば良さそう
"""
from itertools import permutations

N, K = map(int, input().split())
T = [list() for _ in range(N)]
for i in range(N):
    T[i] = list(map(int, input().split()))

ans = 0
for orders in permutations(list(range(N))):
    if orders[0] != 0:
        continue
    circles = list(orders)
    circles.append(0)
    sum_time = 0
    for cur_ind in range(N):
        next_ind = cur_ind + 1
        t = T[circles[cur_ind]][circles[next_ind]]
        sum_time += t
    if sum_time == K:
        ans += 1
print(ans)
