# -*- coding: utf-8 -*-
"""
"""
N = int(input())
S = list(input())

ans_list = [0 for _ in range(N)]

# 一番左から順番に自分より右にいるEの数を数える
sum_e = S.count('E')
for i, s in enumerate(S):
    if s == 'E':
        sum_e -= 1
    ans_list[i] += sum_e

# 一番右から順に自分より左にいるWの数を数える
sum_w = S.count('W')
for i in range(N-1, -1, -1):
    if S[i] == 'W':
        sum_w -= 1
    ans_list[i] += sum_w

print(min(ans_list))
