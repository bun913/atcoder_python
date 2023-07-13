# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from itertools import product

N, M = map(int, input().split())
C = []
for _ in range(M):
    c = int(input())
    A = set(map(int, input().split()))
    C.append(A)

# bit全探索で選ぶ集合を決めれば良い
ans = 0
cond_set = set([i for i in range(1, N + 1)])
for bits in product([True, False], repeat=M):
    # 全てFalseならスキップ
    if not any(bits):
        continue
    s = set()
    for i, bit in enumerate(bits):
        if bit is False:
            continue
        cur_set = C[i]
        # ここが違う
        s = s.union(cur_set)
    if s == cond_set:
        ans += 1
print(ans)
