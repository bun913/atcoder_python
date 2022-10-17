# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from numpy import argsort

N = int(input())
A = list(map(int, input().split()))
ans_list = argsort(A)
[print(a + 1) for a in reversed(ans_list)]
