# -*- coding: utf-8 -*-
"""
解く前のメモ
Nがせいぜい50なので全探索で間に合いそう
"""
N = int(input())
P = list(map(int, input().split()))
expected = sorted(P)

if P == expected:
    print('YES')
    exit()

for i in range(N):
    for j in range(i+1, N):
        a = P[i]
        b = P[j]
        tmp = P[:]
        tmp[i] = b
        tmp[j] = a
        if tmp == expected:
            print('YES')
            exit()
print('NO')
