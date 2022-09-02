# -*- coding: utf-8 -*-
"""
まずは実際に書いてみるか
横は1ずつ異なっているのが並んでいる
縦は7ずつ異なっているのが並んでいる
そして各要素を7で割ったあまりが必ず 1,2,3,4,5,6,0となっているはず
"""
N, M = list(map(int, input().split()))
B = [list(map(int, input().split())) for _ in range(N)]
cycle = [1, 2, 3, 4, 5, 6, 0]
first_ind = cycle.index(B[0][0] % 7)
cycle = cycle[first_ind:]

befs = list(map(lambda elm: elm - 7, B[0]))
for i in range(N):
    for j in range(M):
        v = B[i][j]
        # あまりの数が違うかそもそも無い
        mod = v % 7
        if j > len(cycle) - 1 or mod != cycle[j]:
            print("No")
            exit()
        # 前の行の要素から+7になっていない
        if v != befs[j] + 7:
            print("No")
            exit()
        # 1個左の要素から+1になっていない
        if j > 0:
            if B[i][j - 1] + 1 != v:
                print("No")
                exit()
        # あとは数字の範囲も満たさないといけない
        befs[j] = v
print("Yes")
