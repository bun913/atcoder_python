# -*- coding: utf-8 -*-
"""
解く前のメモ

普通に考えると二重ループで全探索できるが
それだと最大で10**10となるため間に合わない

問題を小さく切り分けて、各要素が自分の1個右だけをみて、その結果を記録しておく
その結果,True(自分より右が自分以下だったマーク)が一番連続している箇所の数を抜き出せば良い
pythonだとgroupby、ランレングス圧縮の考えを利用すれば良さげ
"""
from itertools import groupby

N = int(input())
H = list(map(int, input().split()))

memo = []

# 自分より隣の数が自分以下かをメモ
for i in range(N-1):
    cur = H[i]
    nex = H[i+1]
    if nex <= cur:
        memo.append(1)
        continue
    memo.append(0)

# グループ化
grouped = [(k, list(g)) for k, g in groupby(memo)]
ans = 0
for key, elms in grouped:
    if key == 0:
        continue
    ans = max(ans, len(elms))
print(ans)
