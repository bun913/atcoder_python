# -*- coding: utf-8 -*-
"""
実際に作ってしまう方がわかりやすいかも

まず全部黒に塗る
次に1から始まって2ずつ増やすfor文を作る(7まで)
次に13から始まって2ずつ減らすfor文を作る(7まで)
そこだけ白く塗る
"""

G = [['#' for _ in range(15)] for _ in range(15)]

# 上半分を塗る
for i in range(1, 15, 2):
    for j in range(i, 15-i):
        G[i][j] = '.'

GD = G[:8]
GD = GD[::-1]

rows = G[:7]
rows.extend(GD[:])

for i in range(1, 15):
    n = i + 1
    for j in range(1, 15, 2):
        cur = rows[i][j]
        is_second = False
        if cur == '.':
            if is_second is False:
                for a in range(n, 15-n-1):
                    rows[a][j] = '.'
                is_second = True
                n += 2

for i in range(0, 8):
    for j in range(0, 8):
        cur = rows[i][j]
        rows[i][14-j] = cur

R, C = list(map(int, input().split()))
ans = rows[R-1][C-1]
if ans == '#':
    print('black')
    exit()
print('white')
