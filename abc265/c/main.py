# -*- coding: utf-8 -*-
"""
解く前のメモ
一旦素直にやってみる

無限の判定は0,0に戻るではなく同じマスに戻るだった
"""
H, W = list(map(int, input().split()))
G = [list(input()) for _ in range(H)]

cur = [0, 0]
for _ in range(H * W + 100):
    # 縦軸の動きを最初の要素
    s = G[cur[0]][cur[1]]
    nex = (0, 1)
    if s == 'U':
        nex = (-1, 0)
    elif s == 'D':
        nex = (1, 0)
    elif s == 'L':
        nex = (0, -1)
    # 上下左右にはみ出す場合答えとなる
    nex_x = cur[0] + nex[0]
    nex_y = cur[1] + nex[1]
    if (s == 'U' and cur[0] == 0) or (s == 'D' and cur[0] == H-1) or \
            (s == 'L' and cur[1] == 0) or (s == 'R' and cur[1] == W-1):
        print(cur[0]+1, cur[1]+1)
        exit()
    cur[0] = nex_x
    cur[1] = nex_y
print(-1)
