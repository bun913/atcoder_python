# -*- coding: utf-8 -*-
"""
Aは1..Nまでの要素が並び替えられた数列
連続したK個の要素を選ぶ。選んだ要素の最小値で選んだ要素全てを置き換える。
数列の要素を全て同じにしたい
必要な操作の最小回数を求める

要するにK個ずつのグループを作っていくということだよね
"""
from math import ceil

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
rest = N - K
ans = 1
if rest == 0:
    print(ans)
    exit()
ans += ceil(rest / (K - 1))
print(ans)
