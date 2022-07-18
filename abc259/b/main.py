# -*- coding: utf-8 -*-
"""
三角関数とかベクトルでうまいこと解けそう

今回だと座標の回転なので以下の考えでうまく計算できそう
https://snowtree-injune.com/2021/02/14/rotation-ana009/
"""
from math import radians, cos, sin
import numpy as np

a, b, d = list(map(int, input().split()))

cosd = cos(radians(d))
sind = sin(radians(d))

x = cosd * a - sind * b
y = sind * a + cosd * b
print(x, y)
