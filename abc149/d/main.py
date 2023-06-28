# -*- coding: utf-8 -*-
"""
どのタイミングで勝てる手を出しても最後のポイントは同じ？
K回前に出した手はだせない。つまりこれが困る時ってのは
- K回後にも相手が同じ手を出してくる時
- でもそれって、結局勝ち手となるポイントは同じってこと
- つまりK回あとに勝てる手を出そうとも、その時に勝てる手を出そうとも同じ
てことは、その場その場の最善を尽くしていけば良いということ
"""
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())
hands = []
ans = 0

for i, t in enumerate(T):
    # グー
    if t == 'r':
        if i < K:
            ans += P
            hands.append('p')
        elif hands[i-K] != 'p':
            ans += P
            hands.append('p')
        else:
            # とりあえずどうせ勝てる手が出せないので、それ以外の2手のどちらかというマークをつける
            hands.append('x')
    # チョキ
    if t == 's':
        if i < K:
            ans += R
            hands.append('g')
        elif hands[i-K] != 'g':
            ans += R
            hands.append('g')
        else:
            # とりあえずどうせ勝てる手が出せないので、それ以外の2手のどちらかというマークをつける
            hands.append('x')
    # パー
    if t == 'p':
        if i < K:
            ans += S
            hands.append('s')
        elif hands[i-K] != 's':
            ans += S
            hands.append('s')
        else:
            # とりあえずどうせ勝てる手が出せないので、それ以外の2手のどちらかというマークをつける
            hands.append('x')
print(ans)
