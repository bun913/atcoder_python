# -*- coding: utf-8 -*-
N, M = list(map(int, input().split()))
S = input().split(" ")
T = input().split(" ")

e_stop = set(T)

for s in S:
    ans = 'No'
    if s in e_stop:
        ans = 'Yes'
    print(ans)
