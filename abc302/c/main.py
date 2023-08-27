# -*- coding: utf-8 -*-
"""
解く前のメモ用
問題を勘違いしていた
Sの要素を並び替えるのではなく、Sの順番を並び替えるだけか
"""
from itertools import permutations

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

# 文字数が1の場合はYes
if M == 1:
    print("Yes")
    exit()

for T in permutations(S):
    ok = 0
    for i in range(N-1):
        s1 = T[i]
        s2 = T[i+1]
        diff = sum(el1 != el2 for el1, el2 in zip(s1, s2))
        if diff == 1:
            ok += 1
            continue
    if ok == N-1:
        print("Yes")
        exit()
print("No")
