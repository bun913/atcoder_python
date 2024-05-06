# -*- coding: utf-8 -*-
"""
解く前のメモ用
会議は9:00 ~ 18:00の時間帯で開ける（完全に含まれる場合のみ）
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)

# input
N = int(input())
wx = [list(map(int, input().split())) for _ in range(N)]


def solve():
    ans = -1

    for t in range(0, 25):
        s = 0
        for w, x in wx:
            date_num = (x + t) % 24
            if date_num <= 17 and date_num >= 9:
                s += w
        ans = max(ans, s)

    print(ans)


solve()
