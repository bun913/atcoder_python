# -*- coding: utf-8 -*-
"""
N本の棒がある
i番目の棒の長さはAi
4本の異なる棒を選びそれらの棒を変として長方形を作る
最大の長方形の面積を求める

制約
N <= 10^5
"""
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
items = C.items()
# まず長さの大きい順にソート
long_orderd = sorted(items, reverse=True)
# 次に2本以上ある棒を長さの大きい順にソート
two_or_more = [i for i in long_orderd if i[1] >= 2]

# 作れない場合
if len(two_or_more) <= 1:
    print(0)
    exit()
# 一番長い棒が4本以上
if two_or_more[0][1] >= 4:
    print(two_or_more[0][0]**2)
    exit()
ans = two_or_more[0][0] * two_or_more[1][0]
print(ans)
