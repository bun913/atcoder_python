# -*- coding: utf-8 -*-
"""
N,Mが小さいので二部探索は作らなくてもO(N**2)で十分
"""
N, M = list(map(int, input().split()))
students = [list(map(int, input().split())) for _ in range(N)]
points = [list(map(int, input().split())) for _ in range(M)]

for a, b in students:
    ans = float("inf")
    min_dis = float("inf")
    for i, cd in enumerate(points):
        c, d = cd
        dis = abs(c - a) + abs(d - b)
        if dis < min_dis:
            min_dis = dis
            ans = i + 1
    print(ans)
