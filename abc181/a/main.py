# -*- coding: utf-8 -*-
"""
N個の点のうち3点から一直線になる点は存在するか調べるという話
Nが100個あるので組み合わせなら何とかなるかもしれない

"""
from itertools import combinations

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
print(XY)
