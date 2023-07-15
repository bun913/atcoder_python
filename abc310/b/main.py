# -*- coding: utf-8 -*-
"""
上位互換である条件は以下を全て商品が一つでもあること
- Pi > Pj ようするにj番目の方が安い
- j番目の製品はi番目の製品が持つすべての機能を持つ
- Pi > Pjであるか、j番目の製品はi番目の製品にない機能を1つ以上持つ
"""
N, M = map(int, input().split())
P = []
C = []
functions = []

for _ in range(N):
    p, c, *f = map(int, input().split())
    P.append(p)
    C.append(c)
    functions.append(set(f))

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        # 1つ目の条件
        if P[i] >= P[j]:
            # 2つ目の条件（機能を全て持っているか）
            j_funcs = functions[j]
            i_funcs = functions[i]
            intersect = j_funcs.intersection(i_funcs)
            if len(intersect) == len(i_funcs):
                # 3つ目の条件（jがiにない機能を持っているか）
                if P[i] > P[j] or len(j_funcs) > len(intersect):
                    print("Yes")
                    exit()
print("No")
