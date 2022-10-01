# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N, S = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N)]
