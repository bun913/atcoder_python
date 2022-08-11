# -*- coding: utf-8 -*-
"""
解く前のメモ

いずれの方法でも動かせる数の合計値は2だけ
全ての数の偶奇を合わせて、あとは2ずつ増やしていけば終わりでは
しかも合わせる基準は一番大きい数に合わせればOK
(2ずつ足せば偶奇は絶対に崩れないのであとは数の差だけ)

しかも数が3つなので絶対に1回で偶奇は合わせれるよね
"""
A, B, C = list(map(int, input().split()))
ld = sorted([A, B, C])
is_all_even = all([True if elm % 2 != 0 else False for elm in [A, B, C]])
is_all_odd = all([True if elm % 2 == 0 else False for elm in [A, B, C]])
ans = 0
if is_all_even is False or is_all_even is False:
    odd_count = 0
    for elm in ld:
        if elm % 2 != 0:
            odd_count += 1
    # 奇数が1つなら偶数2つの方を奇数に合わせる
    if odd_count == 1:
        for i in range(3):
            elm = ld[i]
            if elm % 2 == 0:
                ld[i] += 1
        ans += 1
    elif odd_count == 2:
        for i in range(3):
            elm = ld[i]
            if elm % 2 != 0:
                ld[i] += 1
        ans += 1
ld = sorted(ld)
# 全部の偶奇が揃っているならシンプル
ans += (ld[2] - ld[1]) // 2
ans += (ld[2] - ld[0]) // 2
print(ans)
