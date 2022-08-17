# -*- coding: utf-8 -*-
"""
長さNの正しいかっこ列を全て辞書順に出力する

まずNが奇数なら終了
実はNが20なので全列挙でも行けそうではある
正しいカッコ列の判定は?
常に何番目の文字においても(の出現回数が)の出現回数以上となっている状態かな
"""
from itertools import product

N = int(input())
if N % 2 == 1:
    print('')
    exit()

for bits in product(['(', ')'], repeat=N):
    count0 = 0
    count1 = 0
    is_valid = True
    for bit in bits:
        if bit == '(':
            count0 += 1
        else:
            count1 += 1
        if count1 > count0:
            is_valid = False
            break
    if count0 != count1:
        is_valid = False
    if is_valid is False:
        continue
    ans = ''.join(bits)
    print(ans)
