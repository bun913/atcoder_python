# -*- coding: utf-8 -*-
"""
解く前のメモ

N問がかなり大きいので何も考えず全探索は無理
K分間で得られる最大値を求める
DPでN問目までを使って得られる最適解を求め続ければいけそう?

以下解説AC
よく問題をみよう。連続した2分じゃないと満点は取れないとは書いていない。
つまり部分店まで解いて、他の問題、さっきの問題を満点まで取るとかできる

それなら単純に部分点と(満点-部分点)をソートして大きい順に取れば良い
なぜなら部分点の方が満点の半分より大きいことが保証されているため
"""
N, K = list(map(int, input().split()))
points = []
for _ in range(N):
    full, part = list(map(int, input().split()))
    points.append(full-part)
    points.append(part)

soreted_points = sorted(points, reverse=True)
ans = sum(soreted_points[:K])
print(ans)
