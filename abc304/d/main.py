# -*- coding: utf-8 -*-
"""
xy平面上にいくつかのいちごが乗った長方形のケーキがある
ケーキのx軸方向の長さはW、y軸方向の長さはH
ケーキの上にはN個のいちごが乗っている
いちごiは座標(pi,qi)にある。2個以上のイチゴが同一の座標に存在することはない。
Nは最大で2*10**5
このケーキを以下のルールで切り分ける。
ルール1: ケーキを通るy軸に平行なA本の異なる直線x=a1,x=a2,...,x=aAで切る
ルール2: ケーキを通るx軸に平行なB本の異なる直線y=b1,y=b2,...,y=bBで切る
その結果、ケーキは(A+1)*(B+1)個の長方形に分割される
これらの長方形から1ピースをとる時、ピース上にあるいちごの個数として考えられる最大値と最小値を求める
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

# 全ての入力値を受け取る
W, H = list(map(int, input().split()))
N = int(input())
PQ = [list(map(int, input().split())) for _ in range(N)]
A = int(input())
A_list = list(map(int, input().split()))
B = int(input())
B_list = list(map(int, input().split()))
