# -*- coding: utf-8 -*-
"""
取り掛かる前のメモ
横か縦に1づつしか動けないなら、ユークリッド距離が答えになるはず
ただ、問題は無限に広がる空間ということので、探索はできない

約数を列挙して、その中から最も合計が小さい組み合わせを出せば良さげ
Nが10 **12 なのでlogNなら十分間に合うはず
"""

N = int(input())
_min = float('inf')

for d in range(1, int(N ** 0.5) + 1):
    if N % d != 0:
        continue
    q = N // d
    dis = (d-1) + (q-1)
    _min = min(_min, dis)
print(_min)
