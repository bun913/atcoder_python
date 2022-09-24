# -*- coding: utf-8 -*-
"""
"""


def calc(n):
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    if n == 2:
        return [2]
    if n == 3:
        return [1, 2]
    if n == 4:
        return [4]
    if n == 5:
        return [1, 4]
    if n == 6:
        return [2, 4]
    return [1, 2, 4]


A, B = list(map(int, input().split()))
a_list = calc(A)
b_list = calc(B)
uniq = set(a_list + b_list)
print(sum(list(uniq)))
