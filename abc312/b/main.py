# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

# まず開始位置をずらしていく
for i in range(N):
    for j in range(M):
        # 開始位置から8行目したまでいけない場合はスキップ
        # また開始位置から8列足したところにいけない場合も
        if i+8 >= N or j + 8 >= M:
            continue
        ok = True
        # 縦3列,横3列の領域が黒か調べる
        # またそれに隣接する7ますが白か調べる
        for x in range(3):
            for y in range(3):
                # 3ます県内の場合は黒であるべき
                if x <= 2 or y <= 2:
                    if S[i + x][j + y] == '.':
                        ok = False
                # 4ます領域の場合は白じゃないとダメ
                else:
                    if S[i + x][j + y] == '#':
                        ok = False
        # 左上の縦3マス,横3ますが黒じゃなかった
        if ok is False:
            continue
        # else:
        #     print(i, j, "ここまではoK")
        # 右下の3ます領域の一番左上を設定
        a = i + 5
        b = j + 5
        for x in range(4):
            for y in range(4):
                # 一番側の領域は白でないといけない
                if x == 0 or y == 0:
                    if S[a + x][b + y] == '#':
                        ok = False
                        break
                else:
                    if S[a + x][b + y] == '.':
                        ok = False
                        break
        if ok is True:
            print(i+1, j+1)
