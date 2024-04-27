# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def is_kaibun(s: str) -> bool:
    return s == s[::-1]


S = input()

ans = 0
for i in range(0, len(S)):
    for j in range(i, len(S)):
        s = S[i:j+1]
        if is_kaibun(s):
            ans = max(ans, len(s))
print(ans)
