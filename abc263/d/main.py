# -*- coding: utf-8 -*-
"""
解く前のメモ

xは全探索で決める?
yについても、そもそもRがLより小さかったら1にした方が良いに決まっている
1:yは0にした場合の合計値を考える
2: RがL以下の場合はy=1にして限界までかえて、その場合の合計値を考える
3: RがLより大きい場合、xより大きい数のyに限られる
"""

N, L, R = list(map(int, input().split()))
A = list(map(int, input().split()))
# 何もしない状態を答えの初期値とする
ans = sum(A)

for x in range(1, N+1):
    left = A[:x]
    right = A[x:]
    # yを0にして何もしない場合
    cand1 = sum(left) + sum(right)
    cand2 = float('inf')
    cand3 = float('inf')
    # RがL以下の場合、極力Rに変更した方が良い場合
    if R <= L:
        cand2 = L + (R * (N-1))
    # RがLより大きい場合、極力Lを使った方が良い
    else:
        if len(right) > 0:
            cand3 = sum(left) + sum(right) - right[-1] + R
    ans = min([cand1, cand2, cand3])
print(ans)
