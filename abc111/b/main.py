# -*- coding: utf-8 -*-
"""
解く前のメモ

Nが3桁であることはわかっている
あまり難しいことを考えずに最初の桁数をみて、場合分けをすれば良さそう
"""

N = int(input())
first = int(str(N)[0])

most_nearby = 100 * first + 10 * first + first

if N > most_nearby:
    most_nearby = 100 * (first + 1) + 10 * (first + 1) + (first + 1)
print(most_nearby)
