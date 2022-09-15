# -*- coding: utf-8 -*-
"""
各整数に対して1足すか、引くか、何もしない
ai = X となるiの個数を最大化する
うまくXを選んで個数を最大化する

単純に全ての要素で3パターンを試して最頻値を答えにすれば良いだけでは
"""
from collections import defaultdict
from operator import itemgetter

N = int(input())
A = list(map(int, input().split()))

memo = defaultdict(int)

for i in range(N):
    a = A[i]
    minus = A[i] - 1
    plus = A[i] + 1
    memo[a] += 1
    memo[minus] += 1
    memo[plus] += 1

sorted_memo = sorted(memo.items(), key=itemgetter(1), reverse=True)
print(sorted_memo[0][1])
