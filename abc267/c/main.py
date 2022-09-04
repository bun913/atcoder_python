# -*- coding: utf-8 -*-
"""
わざとTLEになる答えを求める
"""
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
# 前の答えを利用するので最初の答えだけ手で出しておく
s1 = 0
for i, v in enumerate(A[:M]):
    s1 += (i + 1) * v
ans_list = [s1]

ans = s1
for i in range(1, N + 1):
    # M先まで見れなくなったら終了
    if i + M > N:
        break
    # 前の答えを今回の答えに利用(S1からS2を求める形)
    bef_ans = ans_list[i - 1]
    # A[i-1]からA[i-1+M-1]までの和を求める
    tmp_list = A[i - 1 : i - 1 + M]
    total = sum(tmp_list)
    # 式に当てはめる
    cur_ans = bef_ans + (A[i + M - 1] * M) - total
    ans_list.append(cur_ans)
    ans = max(ans, cur_ans)
print(ans)
