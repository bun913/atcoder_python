# -*- coding: utf-8 -*-
"""
N問がある時間がTi秒かかる
M種類のドリンクがある。問題Piを解くのがXi秒になる
いずれかのドリンク1個だけ飲める
それぞれのドリンクを飲んだ場合最短何秒で時終わるようになるか知りたい

同じ問題に効果があるドリンクもあるので辞書形式は無理
素直にタプルのリストで保持しておけばよし
"""
N = int(input())
T = list(map(int, input().split()))
M = int(input())
P = [list(map(int, input().split())) for _ in range(M)]
total = sum(T)

for _, L in enumerate(P):
    k = L[0]
    v = L[1]
    ans = total - T[k - 1] + v
    print(ans)
