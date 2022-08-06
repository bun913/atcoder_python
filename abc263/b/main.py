# -*- coding: utf-8 -*-
"""
解く前のメモ

"""

N = int(input())
P = list(map(int, input().split()))

old_gens = set()
PD = P[::-1]
next_ans = 10000

ans = 1
for i in range(N-1):
    n = N-i
    people = PD[i]
    if i == 0:
        next_ans = people
    if n == next_ans:
        ans += 1
        next_ans = people
print(ans)
