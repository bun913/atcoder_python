# -*- coding: utf-8 -*-
"""
解く前のメモ

どうもこうもすでに申請されているユーザー名をsetに持っておいて判定していくだけでは
"""
N = int(input())
memo = set()
ans = []

for i in range(N):
    s = input()
    if s not in memo:
        ans.append(i+1)
    memo.add(s)

for n in ans:
    print(n)
