# -*- coding: utf-8 -*-
"""
一度も連続して並ばなかったら不仲である可能性がある
不仲である可能性がある2人組の個数を求める
NとMが大した数ではないので全ての可能性を求めるか
"""
from itertools import combinations

N, M = map(int, input().split())
all_combi = set(combinations(range(1, N+1), 2))
actual_combi = set()

for _ in range(M):
    A = list(map(int, input().split()))
    # 隣り合った人の組み合わせを求める
    for i in range(N-1):
        actual_combi.add((A[i], A[i+1]))
        actual_combi.add((A[i+1], A[i]))

hunaka_cands = all_combi - actual_combi
ans = len(hunaka_cands)
print(ans)
