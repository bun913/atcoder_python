# -*- coding: utf-8 -*-
"""
行を何行か選び、列を何列か選ぶ。選んだ行と列を全て赤く塗る
黒いマスがK個残るようにできる行と列の選び方はあるか

H,Wが6と非常に少ないのでそれぞれのbit全探索で間に合いそう
"""
from itertools import product
from copy import deepcopy

H, W, K = list(map(int, input().split()))
A = [list("".join(input())) for _ in range(H)]

ans = 0
for row_bits in product([0, 1], repeat=H):
    for col_bits in product([0, 1], repeat=W):
        AD = deepcopy(A)
        cnt = 0
        for i in range(H):
            for j in range(W):
                if row_bits[i] == 1 or col_bits[j] == 1:
                    AD[i][j] = "R"
                # 行を黒くする
                if AD[i][j] == "#":
                    cnt += 1
        if cnt == K:
            ans += 1
print(ans)
