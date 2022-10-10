# -*- coding: utf-8 -*-
"""
取り出したボールの総積がXになるような取り出し方
書かれた数が同じでも区別する
袋に入っているボールの数は10**5を越えない
"""
N, X = list(map(int, input().split()))
ans_lis = [1]

for _ in range(N):
    A = list(map(int, input().split()))
    L = A.pop(0)
    ans_lis = [x * y for x in ans_lis for y in A]
print(ans_lis.count(X))
