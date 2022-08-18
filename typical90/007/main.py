# -*- coding: utf-8 -*-
"""
解く前のメモ

対象レーティングと自分のレーティングとの差が大きいと不満
番号jの生徒の不満どとして考えられる最小値を求める

Nが30万、Qが30万普通に全探索していたら間に合わない
一目見て思った・・・二部探索使えばいいじゃないと
"""
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
AD = sorted(A)
Q = int(input())
B = [int(input()) for _ in range(Q)]

for b in B:
    ans = 0
    ind = bisect_left(AD, b)
    if ind == 0:
        ans = abs(AD[0]-b)
    elif ind == N:
        ans = abs(AD[ind-1]-b)
    else:
        ans = abs(AD[ind]-b)
        ans = min(ans, abs(AD[ind-1]-b))
    print(ans)
