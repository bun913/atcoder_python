# -*- coding: utf-8 -*-
"""
まずM,A,R,C,Hのいずれかで始まる人をフィルター
"""
from collections import Counter
from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    elif r < 0:
        return 0
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


N = int(input())
march_list = []
for _ in range(N):
    S = input()
    if S[0] in set(['M', 'A', 'R', 'C', 'H']):
        march_list.append(S)

C = Counter([s[0] for s in march_list])
# M,A,R,C,Hが被らないように3人選ぶのを全探索
duplicated = set()
ans = 0
for m in ['M', 'A', 'R', 'C', 'H']:
    for a in ['M', 'A', 'R', 'C', 'H']:
        for r in ['M', 'A', 'R', 'C', 'H']:
            if len(set([m, a, r])) == 3:
                sort_list = sorted([m, a, r])
                if tuple(sort_list) in duplicated:
                    continue
                ans += C[m]*C[a]*C[r]
                duplicated.add(tuple(sort_list))
print(ans)
