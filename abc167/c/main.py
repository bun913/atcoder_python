# -*- coding: utf-8 -*-
"""
解く前のメモ
N,Mが最大12と良心的な数になっている
ということはNを選ぶ組み合わせを全探索しても間に合うということ
なので素直に全部のパターンを試して最小値を探すのみ

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""

N, M, X = list(map(int, input().split()))
memo = []
for i in range(N):
    L = list(map(int, input().split()))
    memo.append({'c': L[0], 'A': L[1:]})

ans = float('inf')
for i in range(2**N):
    costs = 0
    understand_scores = [0 for _ in range(M)]
    for j in range(N):
        if ((i >> j) & 1):
            # j番目の参考書を読む
            dic = memo[j]
            cost = dic['c']
            scores = dic['A']
            costs += cost
            for a in range(M):
                understand_scores[a] += scores[a]
    is_score_overs = [True if s >= X else False for s in understand_scores]
    if all(is_score_overs) is True:
        ans = min(ans, costs)
if ans == float('inf'):
    ans = -1
print(ans)
