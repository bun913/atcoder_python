# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
N = int(input())
S = list(input())
T = list(input())


def is_similar(s, t):
    if s == t:
        return True
    if set([s, t]) == set(["1", "l"]):
        return True
    if set([s, t]) == set(["0", "o"]):
        return True


for i in range(N):
    s = S[i]
    t = T[i]
    if not is_similar(s, t):
        print("No")
        exit()
print("Yes")
