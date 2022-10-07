# -*- coding: utf-8 -*-
"""
成績が10の倍数の場合は画面上で成績が0と表示されてしまう
成績として画面に表示されうる最大の値はいくつか

Nが100なのでbit全探索は無理
考えられるものは全部足して10の倍数かどうか判定
"""
N = int(input())
S = [int(input()) for _ in range(N)]

ans = sum(S)

# 10の倍数ではなかった場合
if ans % 10 != 0:
    print(ans)
    exit()

# ここまできたら10の倍数なので
# 引いた結果が10の倍数になるのは引いた数字が10の倍数のみ

for n in sorted(S):
    if n % 10 == 0:
        continue
    print(ans - n)
    exit()
print(0)
