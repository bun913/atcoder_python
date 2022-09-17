# -*- coding: utf-8 -*-
"""
Nが2の60乗と非常に大きいので普通に数え上げるのは無理
Nを2進数に変換して1の部分を0か1に変えた数だけを数え上げれば良い
"""
from itertools import product

S = input()
N = int(S)

B = format(N, "b")

keta_list = []
for i in range(len(B)):
    if B[i] == "1":
        keta_list.append(i)
ans_list = []
for combi in product([True, False], repeat=len(keta_list)):
    tmp = list(B)
    for i, bo in enumerate(combi):
        n = keta_list[i]
        if bo is True:
            tmp[n] = "1"
        else:
            tmp[n] = "0"
    ans_list.append(int("".join(tmp), 2))

for ans in sorted(ans_list):
    print(ans)
