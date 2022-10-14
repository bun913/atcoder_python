# -*- coding: utf-8 -*-
"""
解く前のメモ用
yの縦位置は1個ずつ上がっている
タイプA(0,i) 直線y=a上にあるボールまで移動して、回収して戻る。
タイプB(K,b)
ロボットの移動距離の総和として考えられるものの最小
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N = int(input())
K = int(input())
X = list(map(int, input().split()))

ans = 0
for x in X:
    ans += min(abs(x) * 2, abs(K - x) * 2)
print(ans)
