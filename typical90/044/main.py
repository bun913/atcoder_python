# -*- coding: utf-8 -*-
"""
言われた取りにやるだけじゃね？
と思ったけど、素直に右シフトさせるとdequeとかだと計算が大きすぎるのか

以下解説AC
結局何回シフトさせたかメモしておけば実際にシフトさせなくてもその数が出せるよねというお話
"""
N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
L = A[:]

shift = 0
for i in range(Q):
    q, x, y = list(map(int, input().split()))
    gx = (x - shift-1) % N
    gy = (y - shift-1) % N

    # 1の場合
    if q == 1:
        befx = L[gx]
        befy = L[gy]
        L[gx] = befy
        L[gy] = befx
        continue
    # 2の場合右シフト
    if q == 2:
        shift += 1
        continue
    print(L[gx])
