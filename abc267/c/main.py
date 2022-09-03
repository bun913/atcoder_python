# -*- coding: utf-8 -*-
"""
かける数は1からMって決まっているから全てのパターンを用意できないかな

まず普通に実装して答えがどんな感じで決まるのか見てみよう
とりあえず最初の要素と最後の要素の差が大きいところだけ見てみようか
"""
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = -(10**17)
max_left_ind = 0
max_dif = -(10**17)
bef_left = A[0]
for i in range(N):
    # オーバーするなら終わり
    if i + M - 1 > N - 1:
        break
    tmp = A[i : i + M]
    right_ind = i + M - 1
    right = A[i + M - 1]
    if right_ind - M > 0:
        bef_left = A[right_ind - M]
    max_dif = max(max_dif, right - bef_left)
    if max_dif == right - bef_left:
        max_left_ind = i
tmp = A[max_left_ind : max_left_ind + M]
ans = 0
for i, v in enumerate(tmp):
    ans += (i + 1) * v
print(ans)
