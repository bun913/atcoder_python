# -*- coding: utf-8 -*-
"""
解く前のメモ

X,Yが10**5なので1ループは可能
今回の場合ABピザの枚数が決まれば残りのピザの枚数は勝手に決まる
"""
A, B, C, X, Y = list(map(int, input().split()))

# オーバーキル気味だが十分な回数ABピザの枚数を探索
ans = float('inf')
for ab_cnt in range(0, 2*max(X, Y)+1):
    ab_sum = ab_cnt * C
    a_cnt = max(0, X - (ab_cnt // 2))
    b_cnt = max(0, Y - (ab_cnt // 2))
    a_sum = a_cnt * A
    b_sum = b_cnt * B
    s = a_sum + b_sum + ab_sum
    ans = min(s, ans)
print(ans)
