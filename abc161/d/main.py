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
    q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
    i = 1
    while q:
        if i == K:
            print(q.popleft())
            return
        cur = q.popleft()
        # 自分自身の一番右の桁を-1して次の数を作る(絶対値-1)
        if cur % 10 != 0:
            q.append(cur * 10 + cur % 10 - 1)
        # 自分自身の一番右の桁を足して次の数を作る
        q.append(cur * 10 + cur % 10)
        # 自分自身の一番右の桁を+1して次の数を作る(絶対値+1)
        if cur % 10 != 9:
            q.append(cur * 10 + cur % 10 + 1)
        i += 1


solve()
