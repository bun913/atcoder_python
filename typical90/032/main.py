# -*- coding: utf-8 -*-
"""
解く前のメモ
いかに短くゴールできるか

ただし、XiとYiは仲が悪く前後になることができないとのこと
Nが10と非常に少ないため全探索できそうだが、前後の人に気をつけないといけない感じかな
"""
from itertools import permutations

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())

# 仲が悪い情報をマッピング
ng_set = set()
for _ in range(M):
    X, Y = list(map(int, input().split()))
    X -= 1
    Y -= 1
    ng_set.add(str(X)+str(Y))
    ng_set.add(str(Y)+str(X))

ans = float('inf')
is_ok = False
for order in permutations(range(N), N):
    s = 0
    is_ok_order = True
    for i in range(N):
        cur_runner = order[i]
        cur_cost = A[cur_runner][i]
        # 前の人が嫌いか確認
        if i != 0:
            bef_runner = order[i-1]
            comb = str(cur_runner) + str(bef_runner)
            if comb in ng_set:
                is_ok_order = False
                break
        # 後ろの人が嫌いか確認
        if i != N-1:
            aft_runner = order[i+1]
            comb = str(cur_runner) + str(aft_runner)
            if comb in ng_set:
                is_ok_order = False
                break
        s += cur_cost
    # 嫌いな人がいる並びだった場合
    if is_ok_order is False:
        continue
    is_ok = True
    ans = min(ans, s)

if is_ok is False:
    print(-1)
    exit()
print(ans)
