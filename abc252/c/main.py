# -*- coding: utf-8 -*-
"""
N個のリールからなるスロット
S_i は0..1..9がちょうど1回ずつ現れる長さ10の文字列

制約
2 <= N <= 100
"""
from collections import Counter

N = int(input())
memo = dict([i, []] for i in range(10))
S = []

for _ in range(N):
    s = list(input())
    s = list(map(int, s))
    S.append(s)
    for i in range(10):
        a = s[i]
        memo[a].append(i)
        memo[a].sort()
# 最小の時間を数えていく
ans = float("inf")
for k, L in memo.items():
    new_l = []
    poped = []
    for num in L:
        cnt = poped.count(num)
        new_l.append(num + 10*cnt)
        poped.append(num)
    new_l.sort()
    ans = min(ans, new_l[-1])
print(ans)
