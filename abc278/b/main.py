# -*- coding: utf-8 -*-
"""
解く前のメモ用
見間違えやすい時刻・・・右上と左したを入れ替えても24時間時刻としてみれる
現時点を含める見間違えやすい最初の時刻を求める
Aは0,1,2のいずれか
Bは0以上9以下までのいずれか（でもAが2の時には0以上3以下）
Cは0以上5以下までのいずれか
Dは0以上9以下
"""
from sys import setrecursionlimit
setrecursionlimit(10**7)


def is_confuse_time(h: int, m: int):
    # 見間違いやすい時間の判定
    a = h // 10
    b = h % 10
    c = m // 10
    d = m % 10
    b, c = c, b
    if a == 2:
        if b > 3:
            return False
    if c > 5:
        return False
    return True


H, M = list(map(int, input().split()))
for i in range(60 * 60 * 24):
    if is_confuse_time(H, M):
        print("{} {}".format(H, M))
        exit()
    # 1秒足す
    M += 1
    M %= 60
    if M == 0:
        H += 1
        H %= 24
