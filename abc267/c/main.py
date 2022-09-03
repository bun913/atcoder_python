# -*- coding: utf-8 -*-
"""
普通にやるとTLEになるのは分かっている
前の計算結果とかぶっている区間が多いからそれを利用して解くっぽい
ということまでわかるが実装(式変形)がわからない

以下解説AC
- 前の区間と今の区間を引き算してあげると式が見えてくる(等比数列の和の出し方みたいだなと思った)
"""
from itertools import accumulate
from functools import reduce

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
# N項までの累積和を用意
T = [0] + list(accumulate(A))
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
    bef_ans = ans_list[i - 1]
    cur_total = T[i + M - 1] - T[i - 1]
    # 前の答え - (N+M-1項までの和) + (今回右端に出てきた数*)が今回の求める値となる
    cur_ans = bef_ans + (A[i + M - 1] * M) - cur_total
    ans_list.append(cur_ans)
    ans = max(ans, cur_ans)
print(ans)
