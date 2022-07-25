# -*- coding: utf-8 -*-
"""
DPの典型みたいな問題だと思った

が、どうも考えてみたら罠っぽかった
というのもチーズは普通にどれを何グラム使っても良いわけなのでコスパの良い順に並べて余った文を付け足していけば良いだけ
"""
from operator import itemgetter

N, W = list(map(int, input().split()))
memo = []
for i in range(N):
    a, b = list(map(int, input().split()))
    dic = {'value': a, 'weight': b, 'cosp': a / b}
    memo.append(dic)

_sorted = sorted(memo, key=itemgetter('value'), reverse=True)
ans = 0

for dic in _sorted:
    if W == 0:
        break
    a = dic['value']
    b = dic['weight']
    # bとWの残りの最小値文だけ入れる
    g = min(b, W)
    ans += a * g
    W -= g
print(ans)
