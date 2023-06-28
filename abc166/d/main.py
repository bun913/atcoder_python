# -*- coding: utf-8 -*-
"""
A,Bはそれぞれだかだか10**2/5となる
"""
X = int(input())
limit = int(pow(X, 2/5))
for a in range(-limit, limit+1):
    for b in range(-limit, limit+1):
        if pow(a, 5) - pow(b, 5) == X:
            print(a, b)
            exit()
