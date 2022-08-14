# -*- coding: utf-8 -*-
"""
解く前のメモ

見た感じ最大公約数とか最小公倍数・あまりが関わっていそうな気がする
1辺が最大公約数の立方体ができる

切る回数は((A//G) -1)
※ ここで少し混乱したが考えてみれば当たり前だった・・・
だって、12の長さの棒を4の長さに切り分けるための操作回数は2回だろう
最後に残る部分は切らないで良いのでということだった。単純乙。
(12 // 4)- 1
"""
from math import gcd

A, B, C = list(map(int, input().split()))
G = gcd(A, B)
G = gcd(G, C)

a_cnt = (A // G) - 1
b_cnt = (B // G) - 1
c_cnt = (C // G) - 1
ans = a_cnt + b_cnt + c_cnt
print(ans)
