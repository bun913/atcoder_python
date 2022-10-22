# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用
これは単純にその時々の最適解（できれば差が小さい方）を選び続けるだけでは
"""
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cands = []
for i in range(N - 1):
    a = A[i]
    b = B[i]
    nexa = A[i + 1]
    nexb = B[i + 1]
    # 初回のみ
    if i == 0:
        if min([abs(a - nexa), abs(a - nexb), abs(b - nexa), abs(b - nexb)]) > K:
            print("No")
            exit()
        if abs(a - nexa) <= K:
            cands.append((a, nexa))
        if abs(a - nexb) <= K:
            cands.append((a, nexb))
        if abs(b - nexa) <= K:
            cands.append((b, nexa))
        if abs(b - nexb) <= K:
            cands.append((b, nexb))
        continue
    # 前からみた全ての候補を確認する
    next_cands = []
    for prev, cur in cands:
        if abs(cur - nexa) <= K:
            next_cands.append((cur, nexa))
        if abs(cur - nexb) <= K:
            next_cands.append((cur, nexb))
    cands = next_cands
    # ここで次の候補がなくなっていれば終了
    if len(cands) == 0:
        print("No")
        exit()
print("Yes")
