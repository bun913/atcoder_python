# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from functools import reduce
from itertools import combinations
import math

S = input()

# 大文字が含まれるか判定
# 小文字が含まれるか判定
is_upper = False
is_lower = False
for s in S:
    if s.isupper():
        is_upper = True
    elif s.islower():
        is_lower = True
# 全てユニークな文字列か判定
is_unique = False
if len(set(list(S))) == len(S):
    is_unique = True
if all([is_lower, is_upper, is_unique]):
    print('Yes')
    exit()
print("No")
