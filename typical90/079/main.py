# -*- coding: utf-8 -*-
"""
x,yを自分,一個右,一個上,一個右斜め上を増やすか減らすか

AをBに一致させることができるか
最小の操作回数も

以下解説AC
一個のますずつ合わせていく。そうすると2回目にそのますを含むような範囲でも
それ以上はそのマスの数を変えられないはず。AとBの一致するますを一致させるように数をこなしていくことで
答えが一致するはず
"""
H, W = list(map(int, input().split()))

A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

cnt = 0
for i in range(0, H-1):
    for j in range(0, W-1):
        t = B[i][j] - A[i][j]
        cnt += abs(t)
        A[i][j] += t
        A[i+1][j] += t
        A[i][j+1] += t
        A[i+1][j+1] += t

if A == B:
    print('Yes')
    print(cnt)
    exit()
print('No')
