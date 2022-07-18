# -*- coding: utf-8 -*-
"""
解く前のメモ
Nが10**5で、dが1-**5が最大なのでやろうと思えば、1から数え上げても間に合いそう
でも色々と制限を見ていたたら、必ずNが偶数なので、ソート済みの配列を半分に割って
左側の配列の最後の要素より大きく、右側の配列の最初の要素以下の数を数えれば良さそう
"""

N = int(input())
D = list(map(int, input().split()))
dr = sorted(D)

left = dr[:N//2]
right = dr[N//2:]

le = left[-1]
re = right[0]

ans = max(0, re-le)
print(ans)
