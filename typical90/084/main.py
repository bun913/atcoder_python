# -*- coding: utf-8 -*-
"""
l文字目からr文字目の区間に○とxが両方含まれる
lは決めうちにして、lの文字に応じてrを2分探索で探せばよいのでは
○と罰の位置をあらかじめメモしておけばl移行に初めて出てくるo(またはx)の位置をすぐ出せそう
"""
from bisect import bisect_left

N = int(input())
S = list(input())
o_list = []
x_list = []

for i, s in enumerate(S):
    if s == 'o':
        o_list.append(i)
        continue
    x_list.append(i)

ans = 0
for left in range(N-1):
    cur = S[left]
    search_list = o_list
    if cur == 'o':
        search_list = x_list
    r_ind = bisect_left(search_list, left)
    # 一番右側だったらoかxが見つからなかった
    if r_ind == len(search_list):
        continue
    right = search_list[r_ind]
    cnt = (N-1) - right + 1
    ans += cnt
print(ans)
