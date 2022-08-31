# -*- coding: utf-8 -*-
"""
連続するK個の区画を選んだときそれら区画の資源の総和

累積和の問題っぽい
累積和を出しておく
"""
from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
accum = list(accumulate(A))
accum.insert(0, 0)

max_list = [0 for _ in range(N)]
# iが連続する何個の区画をみるかを示す
for i in range(1, N+1):
    ans = 0
    # jが実際に右端を決めるものとなっている
    for j in range(i, N+1):
        ans = max(ans, accum[j]-accum[j-i])
    print(ans)
