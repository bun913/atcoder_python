# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, box_memo, card_memo = arrange()
    act(N, box_memo, card_memo)


def arrange():
    N = int(input())
    box_memo = {}
    for i in range(N+1):
        box_memo[i] = []
    card_memo = {}
    return N, box_memo, card_memo


def act(N, box_memo, card_memo):
    Q = int(input())
    for _ in range(Q):
        order = input()
        q = list(map(int, order.split(" ")))
        if order.startswith("1"):
            _, i, j = q
            box_memo[j].append(i)
            if i not in card_memo:
                card_memo[i] = set([j])
            else:
                card_memo[i].add(j)
            # print(box_memo, card_memo)
        elif order.startswith("2"):
            i = q[1]
            ans = sorted(box_memo[i])
            print(*ans)
        else:
            q = list(map(int, order.split(" ")))
            i = q[1]
            ans = sorted(card_memo[i])
            print(*ans)


solve()
