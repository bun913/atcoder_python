# -*- coding: utf-8 -*-
"""
解く前のメモ

普通に考えればQ個の質問に答えるようにSを切り出して、それにACが含まれるか判定する
ところが、それだとQ * NとなってしまいTLEになることがわかる

おそらくアプローチとしては、あらかじめACが現れる箇所の開始インデックスをメモしておくことだと思う
が、それをどのように判定すれば少ない計算量でいけるかがわからん

以下解説でわかった
n文字目時点におけるACの出現回数を保持しておけば良い(配列tとする)
そうすればQの各クエリで t[r] - t[l] をすればACの数を重複なしで得ることができる
"""

N, Q = list(map(int, input().split()))
S = input()
t = [0]
ac_cnt = 0

for i in range(1, N):
    bef = S[i-1]
    cur = S[i]
    joined = bef + cur
    if joined == 'AC':
        ac_cnt += 1
    t.append(ac_cnt)

for i in range(Q):
    l, r = list(map(int, input().split()))
    print(t[r-1] - t[l-1])
