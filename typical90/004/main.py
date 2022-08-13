# -*- coding: utf-8 -*-
"""
解く前のメモ

HWが小さければそれぞれのセルに対して、毎回縦方向・横方向にみていけば良い
が、今回はH,Wが最大で2000なのでTLEになることが予想される

そのため、あらかじめ各行・各列の和を算出しておき、それらを足し合わせた数から各セルの重複分を除けばよし
"""
H, W = list(map(int, input().split()))
rows = [list(map(int, input().split())) for _ in range(H)]
cols = [i for i in zip(*rows)]

row_sums = [sum(A) for A in rows]
col_sums = [sum(B) for B in cols]

ans = []
for i in range(H):
    row = []
    for j in range(W):
        cur = rows[i][j]
        row_sum = row_sums[i]
        col_sum = col_sums[j]
        row.append(row_sum + col_sum-cur)
    ans.append(row)

for a in ans:
    print(*a)
