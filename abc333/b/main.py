# -*- coding: utf-8 -*-
"""
解く前のメモ用
正五角形Pが与えられる
A,B,C,D,Eの順で5つの頂点がある
S1,S2,T1,T2 として文字列が与えられる。
S1,S2,T1,T2はそれぞれA,B,C,D,Eのいずれかである
S1,S2,T1,T2の長さが等しい場合はYesを出す
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    S1, S2, T1, T2 = arrange()
    act(S1, S2, T1, T2)


def arrange():
    S1, S2 = list(input())
    T1, T2 = list(input())
    return S1, S2, T1, T2


def act(S1, S2, T1, T2):
    same1 = set([
        "AB",
        "BA",
        "BC",
        "CB",
        "CD",
        "DC",
        "DE",
        "ED",
        "EA",
        "AE"
    ])
    # その他Aを起点に長さが同じもの
    same2 = set([
        "AC",
        "CA",
        "AD",
        "DA",
    ])
    # その他Bを起点に長さが同じもの
    same3 = set([
        "BD",
        "DB",
        "BE",
        "EB",
    ])
    # その他Cを起点に長さが同じもの
    same4 = set([
        "CE",
        "EC",
        "CA",
        "AC",
    ])
    # その他Dを起点に長さが同じもの
    same5 = set([
        "DA",
        "AD",
        "DB",
        "BD",
    ])
    # その他Eを起点に長さが同じもの
    same6 = set([
        "EB",
        "BE",
        "EC",
        "CE",
    ])
    s1 = S1 + S2
    s2 = T1 + T2
    if s1 in same1 and s2 in same1:
        print("Yes")
        exit()
    if s1 in same2 and s2 in same2:
        print("Yes")
        exit()
    if s1 in same3 and s2 in same3:
        print("Yes")
        exit()
    if s1 in same4 and s2 in same4:
        print("Yes")
        exit()
    if s1 in same5 and s2 in same5:
        print("Yes")
        exit()
    if s1 in same6 and s2 in same6:
        print("Yes")
        exit()
    print("No")


solve()
