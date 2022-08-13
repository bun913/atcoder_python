# -*- coding: utf-8 -*-
"""
行列AとBを一致させることができるか

好きな行と列を消せる
てことは、単純にBに出てくる要素がAに全部出てくればOKなのでは

全部消して試せば良かった
"""
from itertools import combinations
from copy import deepcopy

H, W = list(map(int, input().split()))


A = [list(map(int, input().split())) for _ in range(H)]

H2, W2 = list(map(int, input().split()))

B = [list(map(int, input().split())) for _ in range(H2)]

# Aの消す行をコンビネーションで選ぶ(ただし、Bと同じ行数になるように調整)
for rows in combinations(range(H), max(0, H - H2)):
    for cols in combinations(range(W), max(0, W - W2)):
        AD = deepcopy(A)
        for row in sorted(rows, reverse=True):
            AD.pop(row)
        for i in range(len(AD)):
            for col in sorted(cols, reverse=True):
                AD[i].pop(col)
        if AD == B:
            print('Yes')
            exit()
ans = 'No'
print(ans)
