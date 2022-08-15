# -*- coding: utf-8 -*-
"""
解く前のメモ

Q個の操作
t=3のときxi番目のカードに書かれた数を紙に書き出す
t=3で書き出された整数を操作順に出力する

特に配列を探す部分もないのでPythonのlistなら問題なし
"""

Q = int(input())
X = []
numbers = []

for _ in range(Q):
    t, x = list(map(int, input().split()))
    if t == 3:
        numbers.append(X[x-1])
    if t == 1:
        X.insert(0, x)
    if t == 2:
        X.append(x)

for number in numbers:
    print(number)
