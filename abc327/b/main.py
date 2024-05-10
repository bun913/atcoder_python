# -*- coding: utf-8 -*-
"""
解く前のメモ用
A**A = B となるAを求めるわけだが
2**2 = 4
3**3 = 27
4**4 = 256
5**5 = 3125
6**6 = 46656
と非常に数が大きくなっていく。
一方Bは最大で10**18なので、AをBまで全探索する必要はなさそう。
具体的に数を絞って全探索すれば十分。
具体的には20**20ですでに10**18を超えているので、20までで十分。
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    B = arrange()
    act(B)


def arrange():
    B = int(input())
    return B


def act(B):
    for i in range(1, 21):
        if i**i == B:
            print(i)
            exit()
    print(-1)


solve()
