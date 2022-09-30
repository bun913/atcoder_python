# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from math import sqrt

setrecursionlimit(10**7)

ax, ay, bx, by, T, V = list(map(int, input().split()))
n = int(input())

for i in range(n):
    cx, cy = list(map(int, input().split()))
    dis_a_to_c = (cx - ax) ** 2 + (cy - ay) ** 2
    dis_c_to_b = (bx - cx) ** 2 + (by - cy) ** 2
    far_to_dis = sqrt(dis_a_to_c) + sqrt(dis_c_to_b)
    if far_to_dis <= T * V:
        print("YES")
        exit()
print("NO")
