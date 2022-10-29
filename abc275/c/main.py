# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
import numpy as np
from itertools import combinations
from math import isclose

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
    # 4つの角が全て等しく、4つの変が全て等しい
    a = np.array(pattern[0])
    b = np.array(pattern[1])
    c = np.array(pattern[2])
    d = np.array(pattern[3])
    # どれかのベクトルの大きさが等しい
    abcd = isclose(np.linalg.norm(b - a), np.linalg.norm(d - c))
    acbd = isclose(np.linalg.norm(c - a), np.linalg.norm(d - b))
    adbc = isclose(np.linalg.norm(d - a), np.linalg.norm(c - b))
    # 角度が等しい
    ab = b - a
    cd = d - c
    tan1 = isclose(np.arctan2(ab[0], ab[1]), np.arctan2(cd[0], cd[1]))
    ac = c - a
    bd = d - b
    tan2 = isclose(np.arctan2(ac[0], ac[1]), np.arctan2(bd[0], bd[1]))
    ad = d - a
    bc = c - b
    tan3 = isclose(np.arctan2(ad[0], ad[1]), np.arctan2(bc[0], bc[1]))
    if (abcd and tan1) or (acbd and tan2) or (adbc and tan3):
        ans += 1
print(ans)
