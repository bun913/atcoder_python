# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

S = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
N = int(input())
print("3." + S[:N])
