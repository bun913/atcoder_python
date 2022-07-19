# -*- coding: utf-8 -*-
"""
解く前のメモ

1個りんごを食べた
N個のりんごを全て材料にした時の味と
N-1個のりんごを材料としてできるものの味の差の絶対値ができるだけ小さくする

食べるりんごを一つ選ぶわけだが、単純に絶対値が最も小さい値を選べば良いみたい
"""

N, L = list(map(int, input().split()))
A = [L + i for i in range(N)]

abs_min = float('inf')
eat_target = -202
for i in range(N):
    a = A[i]
    absa = abs(a)
    abs_min = min(absa, abs_min)
    if abs_min == absa:
        eat_target = i
copy = A[:]
copy.pop(eat_target)
print(sum(copy))
