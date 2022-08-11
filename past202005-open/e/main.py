# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
N, M, Q = list(map(int, input().split()))
# グラフを2次元配列として用意(無向グラフ)
G = [[] for _ in range(N)]

for i in range(M):
    a, b = list(map(int, input().split()))
    G[a-1].append(b-1)
    G[b-1].append(a-1)

# 色を格納
colors = list(map(int, input().split()))


def q1(n: int) -> None:
    # グラフで繋がっている頂点の色を塗り替える
    color = colors[n]
    g = G[n]
    for i in range(len(g)):
        vet = g[i]
        colors[vet] = color


def q2(n: int, override: int) -> None:
    colors[n] = override


# 順番にクエリを実行
for i in range(Q):
    # print('q:{}'.format(i+1))
    L = list(map(int, input().split()))
    vet = L[1] - 1
    print(colors[vet])
    # クエリに応じた処理
    if L[0] == 2:
        override = L[2]
        q2(vet, override)
        continue
    q1(vet)
