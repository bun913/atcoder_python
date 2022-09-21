# -*- coding: utf-8 -*-
"""
整数N
Nの各桁の数字を取り出して並べる
0から始めることはできない
適切にNを分離した時分離後の2数の積の最大値

Nが最高でも9桁なのでbit全探索で左辺と右辺に分ければ良い
あとはそれぞれを降順にソートして計算すればよし
"""
from itertools import product

N = int(input())
S = str(N)

ans = -1
for case_list in product([True, False], repeat=len(S)):
    left = []
    right = []
    for i, is_left in enumerate(case_list):
        if is_left is True:
            left.append(S[i])
            continue
        right.append(S[i])
    if len(left) == 0 or len(right) == 0:
        continue
    if left[0] == "0" or right[0] == "0":
        continue
    ls = "".join(sorted(left, reverse=True))
    rs = "".join(sorted(right, reverse=True))
    ans = max(ans, int(ls) * int(rs))
print(ans)
