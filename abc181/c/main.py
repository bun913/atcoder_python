# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用
N個の3点で同一直線上にあるもの同一直線上にあるものは存在するか
Nが少ないので3点は問題なく全探索できる
傾きが同じか考える
x2- x1 / y2 -y1 = x3 - x2 / y3 - y2
x2 - x1 * y3 - y2 = x3 - x2 * y2 - y1
"""


def is_same_line(a: tuple(), b: tuple(), c: tuple()) -> bool:
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    is_same = (x2 - x1) * (y3 - y2) == (x3 - x2) * (y2 - y1)
    return is_same


N = int(input())
xy = []
for _ in range(N):
    xy.append(tuple(map(int, input().split())))

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if is_same_line(xy[i], xy[j], xy[k]):
                print('Yes')
                exit()
print('No')
