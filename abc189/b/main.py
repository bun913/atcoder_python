# -*- coding: utf-8 -*-
"""
Pは全て%の整数値でくるので、整数で管理しが方が良さそう
"""
N, X = map(int, input().split())
rest = X * 100
for i in range(N):
    v, p = map(int, input().split())
    rest -= v * p
    if rest < 0:
        print(i+1)
        exit()
print(-1)
