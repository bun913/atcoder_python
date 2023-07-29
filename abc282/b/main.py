# -*- coding: utf-8 -*-
"""
2人で協力することで全部の問題を解ける組み合わせの数
i,jともにせいぜい2桁なので全ての組み合わせを出せばOK
"""
from sys import setrecursionlimit
# import combinations
from itertools import combinations

setrecursionlimit(10**7)
N, M = list(map(int, input().split()))
S = [input() for _ in range(N)]

ans = 0
for i, j in combinations(range(N), 2):
    a = S[i]
    b = S[j]
    ok_cnt = 0
    for k in range(M):
        if a[k] == 'o' or b[k] == 'o':
            ok_cnt += 1
    if ok_cnt == M:
        ans += 1
print(ans)
