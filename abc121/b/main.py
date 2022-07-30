# -*- coding: utf-8 -*-
"""
解く前のメモ

Ai1 * B1 + ....と全ての数を掛け合わせれば良いみたい
NもMも20が最大だから間に合いそう
"""

N, M, C = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0

for i in range(N):
    A = list(map(int, input().split()))
    _sum = 0
    for j in range(M):
        a = A[j]
        b = B[j]
        _sum += a * b
    if _sum + C > 0:
        ans += 1
print(ans)
