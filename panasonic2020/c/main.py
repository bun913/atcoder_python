# -*- coding: utf-8 -*-
"""
sqrt(a) + sqrt(b) < sqrt(c)かどうかを求める
このままだと少数の計算となるため、整数の問題に帰結させる
"""
a, b, c = map(int, input().split())
if 4 * a * b < (c - a - b)**2 and c - a - b > 0:
    print("Yes")
    exit()
print("No")
