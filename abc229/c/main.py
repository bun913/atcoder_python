# -*- coding: utf-8 -*-
"""
N種類のチーズ
ピザの美味しさはピザに載せたチーズの美味しさの総和で決まる
載せたチーズの重さは合計でW[g]以下である必要
可能なピザの美味しさの最大値をもとめる
コスパのよいチーズを選び続ける
"""
N, W = map(int, input().split())
c_list = []
for _ in range(N):
    c, w = map(int, input().split())
    c_list.append((c, w))
c_list.sort(reverse=True)

ans = 0
for score, weight in c_list:
    if W >= weight:
        W -= weight
        ans += score * weight
    else:
        ans += score * W
        break
print(ans)
