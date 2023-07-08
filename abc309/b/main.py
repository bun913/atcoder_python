# -*- coding: utf-8 -*-
"""
N*Nの正方形の盤面がある
盤面の各ますは0か1が書かれている
一番外側の辺の数字を時計回りに1つずつずらす
そのずらした後の盤面を出力する
"""
from copy import deepcopy

N = int(input())
A = [list(input()) for _ in range(N)]
B = deepcopy(A)

for i in range(N):
    for j in range(N):
        # 一番外側の辺にならないますはスキップ
        if i == 0 or j == 0 or i == N-1 or j == N-1:
            # 一番上の行は右にずらす
            if i == 0 and j != N-1:
                B[i][j+1] = A[i][j]
            # 一番右の列は下にずらす
            if j == N-1 and i != N-1:
                B[i+1][j] = A[i][j]
            # 一番下の行は左にずらす
            if i == N-1 and j != 0:
                B[i][j-1] = A[i][j]
            # 一番左の列は上にずらす
            if j == 0 and i != 0:
                B[i-1][j] = A[i][j]
for b in B:
    print(''.join(b))
