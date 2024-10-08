# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    act()


def act():
    N = int(input())
    D = len(str(N))

    def recursive(cur, use3, use5, use7):
        if cur > N:
            return 0
        # カウントを増やす
        count = 0
        if use3 and use5 and use7:
            count += 1
        # 3, 5, 7を使う
        count += recursive(cur * 10 + 3, True, use5, use7)
        count += recursive(cur * 10 + 5, use3, True, use7)
        count += recursive(cur * 10 + 7, use3, use5, True)

        return count

    ans = recursive(0, False, False, False)
    print(ans)


solve()
