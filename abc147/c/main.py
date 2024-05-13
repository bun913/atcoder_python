# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, A, xy = arrange()
    ans = act(N, A, xy)
    print(ans)


def arrange():
    N = int(input())
    A = []
    xy = []
    for i in range(N):
        a = int(input())
        A.append(a)
        tmp = []
        for j in range(a):
            x, y = map(int, input().split())
            tmp.append((x, y))
        xy.append(tmp)
    return N, A, xy


def act(N, A, xy):
    ans = 0
    for i in range(2**N):
        cands = [0]*N  # 1を正直者と仮定したリスト
        is_mujyun = False
        for j in range(N):
            # j番目の人を正直者と仮定する場合
            if i >> j & 1:
                cands[j] = 1
            else:
                cands[j] = 0
        # ここまででcands[i]で正直ものと仮定したリストができた（矛盾するとおかしい）
        for k in range(N):
            if i >> k & 1:
                for x, y in xy[k]:
                    # 証言と矛盾する場合
                    if cands[x-1] != y:
                        is_mujyun = True
        if is_mujyun is False:
            ans = max(ans, sum(cands))
    return ans


solve()
