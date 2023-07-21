# -*- coding: utf-8 -*-
"""
時計の右上と左下を入れ替えても時刻として成立するのを間違いやすい時刻とする
初めて訪れる見間違いやすい時刻を求める
"""
H, M = map(int, input().split())

for i in range(0, 3601):
    # 繰り上げる
    m = M + i
    h = H
    if m >= 60:
        h += m // 60
        m %= 60
    h %= 24
    a = h // 10
    b = h % 10
    c = m // 10
    d = m % 10
    b, c = c, b
    if a == 2:
        if b <= 3 and c <= 5 and d <= 9:
            print(h, m)
            exit()
    if a <= 1 and b <= 9 and c <= 5 and d <= 9:
        print(h, m)
        exit()
