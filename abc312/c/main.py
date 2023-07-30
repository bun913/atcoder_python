# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from bisect import bisect_right
from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sellers = sorted(A)
sellers_dict = defaultdict(int)
for seller in sellers:
    sellers_dict[seller] += 1
sellers = sorted(list(set(sellers)))
buyers = sorted(B)
inf = 10 ** 30
ans = inf
seller_cnt = 0
for i, sell_price in enumerate(sellers):
    cur_seller_cnt = sellers_dict[sell_price]
    seller_cnt += cur_seller_cnt
    # 二部探索でsell_priceであれば買ってくれる人の数を確認
    buyer_ind = bisect_right(buyers, sell_price)
    buyer_cnt = M - buyer_ind
    if seller_cnt >= buyer_cnt:
        ans = min(ans, sell_price)
# エッジケース
# 売り手の中で最安値が買い手の中で最高値より高い場合
# この場合どうせ売り手が0人になるため最安のXは買い手の最高価格+1になる
if ans == sellers[0] and ans > buyers[-1]:
    ans = buyers[-1] + 1
print(ans)
