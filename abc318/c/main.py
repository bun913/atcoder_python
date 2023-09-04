# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from itertools import accumulate

N, D, P = map(int, input().split())
F = list(map(int, input().split()))

# まず最も単純な全て通常料金と、全て周遊料金の場合を求めておく
normal = sum(F)
unit = N // D if N % D == 0 else N // D + 1
circular = unit * P
ans = min(normal, circular)

# ここから一部周遊を使うケースを検証する
# 降順にソート
fee_list = sorted(F, reverse=True)
ruiseki = list(accumulate(fee_list))

i = D-1  # 累積和のインデックス
u = 1  # 周遊パスの数
while i < N:
    s = ruiseki[i]
    c_fee = u * P
    n_fee = normal - s
    ans = min(ans, c_fee + n_fee)
    i += D
    u += 1
print(ans)
