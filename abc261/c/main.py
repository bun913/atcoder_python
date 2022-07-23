# -*- coding: utf-8 -*-
"""
解く前のメモ

辞書で持っておけばよいだけじゃね
1ループで終わるし、間に合いそう
"""

N = int(input())
memo = {}

for i in range(N):
    s = input()
    # なければ入れるだけ
    if s not in memo:
        memo[s] = 1
        print(s)
        continue
    # ある場合加工する
    x = str(memo[s])
    result = "{}({})".format(s, x)
    memo[s] += 1
    print(result)
