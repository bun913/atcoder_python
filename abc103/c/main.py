# -*- coding: utf-8 -*-
"""
最小公倍数-1が答えじゃないか
最小公倍数の時に全てのあまりが0になる
てことはそこから-1すれば各要素とのあまりが最大になりそう

RE・・・
よく考えればaが10**5なので最悪LCMがとんでもない数になる
この考え方だけ使って、あとはai-1を足し合わせた方が良さそう
"""
from functools import reduce

N = int(input())
A = list(map(int, input().split()))

ans = reduce(lambda bef, cur: bef + (cur - 1), A, 0)
print(ans)
