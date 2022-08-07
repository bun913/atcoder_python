# -*- coding: utf-8 -*-
"""
解く前のメモ

循環するリストの扱いの練習ぽい問題
ケーキのある連続するピースを選ぶ方法で、選んだぶぶが全体の大きさのちょうど10分の1になるものが存在するか

ただ円形なので用意するリストは2個繋げて、最後の1個だけpopしておけば良い

↓ここからTLEになるので解説見たり
開始位置は全探索で求める
終わり位置はsort済みの配列を渡して2分探索で求めると間に合う
累積和を求めておけばスムーズ

"""
from itertools import accumulate
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

if sum(A) % 10 != 0:
    print('No')
    exit()

target = sum(A) // 10


# 2個繋げて最後の要素だけ不要(最後のピースから1週できるようにする)
cakes = A + A

c_sum = list(accumulate(cakes))

for l in range(N):
    if cakes[l] == target:
        print('Yes')
        exit()
    # 2分探索でrを決める
    # 要は累積話の配列からどこが一番近い数値となるか探している
    # target + これまでの長さとすることで、どの位置に挿入すべきかわかる
    r = bisect_left(c_sum, target + c_sum[l])
    if c_sum[r] - c_sum[l] == target:
        print('Yes')
        exit()
print('No')
