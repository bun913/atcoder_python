# -*- coding: utf-8 -*-
"""
四角形が凸であるか判定
四角形の内角が全て180度未満であるとき
"""
import numpy as np
import math

A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))
C = np.array(list(map(int, input().split())))
D = np.array(list(map(int, input().split())))

# ABCとBCDとCDAとDABの4つの角が全て180度であればよい


def nasukaku(cent, left, right):
    vec1 = [left[0]-cent[0], left[1]-cent[1]]
    vec2 = [right[0]-cent[0], right[1]-cent[1]]
    absvec1 = np.linalg.norm(vec1)
    absvec2 = np.linalg.norm(vec2)
    inner = np.inner(vec1, vec2)
    cos_theta = inner/(absvec1*absvec2)
    theta = np.degrees(np.arccos(cos_theta))
    return theta


ABC = nasukaku(B, A, C)
BCD = nasukaku(C, B, D)
CDA = nasukaku(D, C, A)
DAB = nasukaku(A, D, B)

# print(ABC, BCD, CDA, DAB)
if ABC < 180 and BCD < 180 and CDA < 180 and DAB < 180:
    if math.isclose(ABC+BCD+CDA+DAB, 360.0) is False:
        print('No')
        exit()
# 対角の合計が180度
print('Yes')
