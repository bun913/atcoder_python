# -*- coding: utf-8 -*-
"""
N =200なので3点の全ての組み合わせを全列挙することができる
あとは3点が三角形になるかを判定する必要がある

そういえばベクトルの外積が平方四辺形の面積と等しくなると聞いたことがある
これを半分にすれば三角形の面積になるはずでは
"""
from itertools import combinations

N = int(input())
points = combinations([i for i in range(N)], 3)

dots = [list(map(int, input().split())) for i in range(N)]

ans = 0
for a, b, c in points:
    a_dot = dots[a]
    b_dot = dots[b]
    c_dot = dots[c]
    area = abs(
        (a_dot[0] - c_dot[0]) * (b_dot[1] - c_dot[1])
        - ((b_dot[0] - c_dot[0]) * (a_dot[1] - c_dot[1]))
    )
    if area > 0:
        ans += 1
print(ans)
