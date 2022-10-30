# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from itertools import combinations

S = [list(input()) for _ in range(9)]

# ポーンの点を抽出
porns = []
for x in range(9):
    for y in range(9):
        if S[x][y] == "#":
            porns.append([x, y])
# あとはこの4点が正方形か判定する
ans = 0
for pattern in combinations(porns, 4):
    # 4辺の長さが等しく対角線の長さも等しいと正方形
    dis_of_sides = set()
    for p1, p2 in combinations(pattern, 2):
        dis_of_sides.add((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    if len(dis_of_sides) == 2:
        ans += 1
print(ans)
