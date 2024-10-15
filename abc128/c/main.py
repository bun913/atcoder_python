# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    act()


def act():
    N, M = map(int, input().split())
    switch_has_lights = [[] for _ in range(N)]
    for i in range(M):
        k, *S = map(int, input().split())
        for s in S:
            switch_has_lights[s-1].append(i)
    # 電気がスイッチの偶奇どっちで転倒するか
    P = list(map(int, input().split()))

    ans = 0
    for i in range(2**N):
        switches = []
        for j in range(N):
            if i >> j & 1:
                switches.append(True)
            else:
                switches.append(False)
        lights_even_odd = [0] * M
        for k in range(N):
            lights = switch_has_lights[k]
            if switches[k] is True:
                for light in lights:
                    lights_even_odd[light] += 1
                    lights_even_odd[light] %= 2
        # 最後にスイッチの偶奇を照らし合わせて全部点灯しているか確認
        if lights_even_odd == P:
            ans += 1
    print(ans)


solve()
