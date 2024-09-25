# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""

from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    act()


def act():
    S = list(map(int, list(input())))
    n = len(S)
    ans = 0
    # 区切り位置を求める
    for i in range(2**(n-1)):
        dividors = []
        for j in range(n-1):
            if i >> j & 1:
                dividors.append(j+1)
        if len(dividors) == 0:
            continue
        nums = []
        bef = 0
        for div_ind in dividors:
            nums.append(S[bef:div_ind])
            bef = div_ind
        nums.append(S[bef:])
        # numsに区切ったあとの配列が入っているので足し合わせる
        for num in nums:
            converted = int("".join(map(str, num)))
            ans += converted
    ans += int("".join(map(str, S)))
    print(ans)


solve()
