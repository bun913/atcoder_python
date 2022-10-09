# -*- coding: utf-8 -*-
"""
queryが10**5で操作回数のxが10**5あるので、普通にqueでやると間に合わない
操作は末尾を削除して先頭に挿入するだけなので、ローテーションしている
実際に動かさなくても何回操作したか分かれば答えを導ける
"""
N, Q = list(map(int, input().split()))
S = input()

start = 0
for _ in range(Q):
    t, x = list(map(int, input().split()))
    if t == 1:
        # 添字のスタート位置を左にずらしていしくイメージ
        start -= x
        # N以上はローテーションするためmodを取る
        start %= N
        continue
    # スタート位置がrだけ右にずれている
    i = (start + (x - 1)) % N
    print(S[i])
