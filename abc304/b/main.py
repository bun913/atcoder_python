# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)
N = int(input())
if N <= 10**3 - 1:
    print(N)
    exit()
if N <= 10**4 - 1:
    # 1の位を切り捨てて出力
    print(N // 10 * 10)
    exit()
if N <= 10**5 - 1:
    # 10の位を切り捨てて出力
    print(N // 100 * 100)
    exit()
if N <= 10**6 - 1:
    # 100の位を切り捨てて出力
    print(N // 1000 * 1000)
    exit()
if N <= 10**7 - 1:
    # 1000の位を切り捨てて出力
    print(N // 10000 * 10000)
    exit()
if N <= 10**8 - 1:
    # 10000の位を切り捨てて出力
    print(N // 100000 * 100000)
    exit()
if N <= 10**9 - 1:
    # 100000の位を切り捨てて出力
    print(N // 1000000 * 1000000)
    exit()
