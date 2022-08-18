# -*- coding: utf-8 -*-
"""
解く前のメモ

全員が別の学校に通うようにしたい
家から学校までの距離をEiおして不便さは距離の総和
どの生徒も学校に通う時の不便さとして考えられる最小値を求める

Nが最大100,000なのでbit全探索では無理
ソートっぽい
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
AD = sorted(A)
BD = sorted(B)
for i in range(N):
    a = AD[i]
    b = BD[i]
    ans += abs(a-b)
print(ans)
