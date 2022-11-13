# -*- coding: utf-8 -*-
"""
解く前のメモ用
好き・嫌いのパターン
好き・嫌い・大好きのパターン
"""
N = int(input())
ans = 0
A = list(map(int, input().split()))
for a in A:
    t = a
    while t % 2 == 0 or t % 3 == 2:
        t -= 1
        ans += 1
print(ans)
