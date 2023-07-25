# -*- coding: utf-8 -*-
"""
文字列Sに対して.をXに置き換える操作をK回以下行うことができる
Xを最大で何個連続させることができるか
Sが2*10**5なのでbit全探索は無理
"""
from itertools import accumulate

S = input()
K = int(input())
L = [0]
for s in S:
    if s == "X":
        L.append(0)
        continue
    L.append(1)

counter = list(accumulate(L))

ans = 0
r = 1
for l in range(1, len(counter)):
    while r < len(counter) and counter[r] - counter[l - 1] <= K:
        r += 1
    # 求めるものが区間の数なのでr-lで答えを求める
    ans = max(ans, r-l)
print(ans)
