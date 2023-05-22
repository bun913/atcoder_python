# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)
S = input()
N = len(S)

if N != 8:
    print("No")
    exit()
# 1文字目が大文字でない場合はNG
if S[0].isupper() is False:
    print("No")
    exit()
# 2から7文字目が数値に変換できるか
if S[1:7].isdecimal() and S[1] != "0":
    if S[-1].isupper():
        print("Yes")
        exit()
    print("No")
    exit()
print("No")
