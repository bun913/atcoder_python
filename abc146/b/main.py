# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from functools import reduce, lru_cache
from itertools import combinations
import math

N = int(input())
S = input()


def rot_n(s, n) -> str:
    """
    アルファベットsをn文字分後にずらす
    """
    answer = ''
    for letter in s:
        answer += chr(ord('A') + (ord(letter)-ord('A')+n) % 26)
    return answer


ans = rot_n(S, N)

print(ans)
