# -*- coding: utf-8 -*-
"""
解く前のメモ

N種類を最低1は作る
制約を守ることは可能な入力が渡される
ということはまずmの合計から最低1種類を作るのに必要な量を求めて、そのあまりで最小のmiを持つドーナツを量産する
"""

N, X = list(map(int, input().split()))
M = [int(input()) for _ in range(N)]

# 1種類ずつ作る
ans = len(M)
rest = X - sum(M)

# 最小のやつを作れるだけ作る
_min = min(M)
ans += rest // _min
print(ans)
