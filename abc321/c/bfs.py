# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from collections import deque

setrecursionlimit(10**8)


def solve():
    act()


def act():
    K = int(input())
    i = 1
    q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
    while q:
        cur = q.popleft()
        # 基底条件
        if i == K:
            print(cur)
            return
        # 今の1のくらいの数より小さい数を候補に追加していく
        lim = int(str(cur)[-1])
        for n in range(lim):
            q.append(cur*10 + n)
        i += 1


solve()
