# -*- coding: utf-8 -*-
"""
解く前のメモ用
0と9を含む数列の数を数える
数列全部の数から条件を満たさないものを引いた方が簡単
"""
N = int(input())
# Nが1のエッジケース
if N == 1:
    print(0)
    exit()
# N**10乗が全体の数だが
mod = 10**9+7
al = pow(10, N, mod)
# 0または9を含まない数列の数を数える
# 0を含まない数列の数
dec0 = pow(9, N, mod)
dec9 = pow(9, N, mod)
# 0も9も含まない数列の数
dec09 = pow(8, N, mod)
ans = (al - dec0 - dec9 + dec09) % mod
print(ans)
