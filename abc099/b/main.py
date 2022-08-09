# -*- coding: utf-8 -*-
"""
解く前のメモ

雪が積もった状態での塔の高さがaとb
雪自体の高さをxとしてxの値を求める

違いに1メートル離れたある等のことなので仮にi番目の塔だとすると
b = a + iである

999本しかないから余裕で全探索できる
"""
a, b = list(map(int, input().split()))

for i in range(1, 999):
    i_height = i * (1 + i) // 2
    j_height = (i+1) * (1 + i + 1) // 2
    a_dif = a - i_height
    b_dif = b - j_height
    if a_dif == b_dif:
        print(-a_dif)
