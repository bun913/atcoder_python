# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
N = int(input())
A = list(map(int, input().split()))
ad = [(t, i + 1) for i, t in enumerate(A)]
ad = sorted(ad, reverse=True)
[print(i) for _, i in ad]
