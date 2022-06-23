# -*- coding: utf-8 -*-
N, K = map(int, input().split())
constraints = [0] * (N + 1)
can_num = 0
for _ in range(K):
    c, k = input().split()
    constraints[int(k)] = c
    if c == "R":
        can_num += 1
MOD = 998244353

ans = 1
# カードを左端から右へ向けて順に見ていく
for i in range(1, N + 1):
    # 今のカードのインデックスに制約があるか？無いか？をチェック
    if constraints[i]:
        # 制約があるなら今のカードのインデックスの数は既に指定されている(候補が１つしか無い)
        # 加えて候補となる数の種類が変化する
        if constraints[i] == "L":
            can_num += 1
        else:
            can_num -= 1

    # 今のカードのインデックスでの制約が無いなら候補数を掛け算する
    else:
        ans *= can_num
        ans %= MOD

print(ans)
