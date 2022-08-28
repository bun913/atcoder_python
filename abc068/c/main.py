# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
N, M = list(map(int, input().split()))
G = {}
for _ in range(M):
    a, b = list(map(int, input().split()))
    if a not in G:
        G[a] = set()
    G[a].add(b)
    if b not in G:
        G[b] = set()
    G[b].add(a)
# Nと直接繋がっている島を全部探索する
if N not in G:
    print('IMPOSSIBLE')
    exit()
direct = G[N]
for island in direct:
    if 1 in G[island]:
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')
