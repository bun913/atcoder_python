# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

かたむきが同じか判定する
y1/x1 = y2/x2
x2*y1 = x1*y2
"""
from itertools import combinations


def is_on_line(a, b, c):
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    cx, cy = c[0], c[1]
    fx, fy = bx - ax, by - ay
    sx, sy = cx - ax, cy - ay
    if fx * sy == sx * fy:
        return True
    return False


N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

for a, b, c in combinations([i for i in range(N)], 3):
    # 3点が同じか判定する
    if is_on_line(XY[a], XY[b], XY[c]) is True:
        print("Yes")
        exit()
print("No")
