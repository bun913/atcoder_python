# -*- coding: utf-8 -*-
"""
解く前のメモ

文字列を1言って、青いカードにその文字列が書かれていれば1円もらえる
赤いカードに書かれていれば1円失う(これらは文字列の完全一致のみ)
最大で何円もらうことができるか

dictに何を言えばいくら儲かるか持たせておけばそれが一番大きいものを言えば良さそう
"""
from collections import defaultdict

N = int(input())
memo = defaultdict(int)

for _ in range(N):
    s = input()
    memo[s] += 1

M = int(input())
for _ in range(M):
    s = input()
    memo[s] -= 1

sorted_memo = sorted(memo.items(), key=lambda kv: kv[1], reverse=True)
most_big = sorted_memo[0][1]
ans = max(most_big, 0)

print(ans)
