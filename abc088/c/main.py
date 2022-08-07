# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from itertools import combinations, product
import sys
input = sys.stdin.readline
def iinput(): return int(input())
def sinput(): return input().rstrip()
def i0input(): return int(input()) - 1
def linput(): return list(input().split())
def liinput(): return list(map(int, input().split()))
def miinput(): return map(int, input().split())
def li0input(): return list(map(lambda x: int(x) - 1, input().split()))
def mi0input(): return map(lambda x: int(x) - 1, input().split())


C = []
for _ in [0] * 3:
    C.append(liinput())

for A in product(range(101), repeat=3):
    flg = True
    for j in range(3):
        if not (C[0][j] - A[0] == C[1][j] - A[1] == C[2][j] - A[2]):
            flg = False
            break
    if flg:
        print('Yes')
        exit()
print('No')
