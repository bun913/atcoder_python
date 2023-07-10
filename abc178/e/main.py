# -*- coding: utf-8 -*-
"""
異なる2点間のマンハッタン距離として考えられる最大値
Nが2*10**5なので、全探索は無理
マンハッタン距離はチェビシェフ距離とも呼ばれる
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

point_x_conv = []
point_y_conv = []
for x, y in points:
    point_x_conv.append(x + y)
    point_y_conv.append(x - y)
# x座標側の絶対値とy座標側の絶対値の最大値が答え
x_dist_max = abs(max(point_x_conv) - min(point_x_conv))
y_dist_max = abs(max(point_y_conv) - min(point_y_conv))
print(max(x_dist_max, y_dist_max))
