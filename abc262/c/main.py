# -*- coding: utf-8 -*-
"""
解く前のメモ

普通にやるならiとjをそれぞれ二重ループで全探索
だが、Nが10**5まであるのでi<jとなる組を数えるとTLEとなってしまう

以下解説AC
ここでどのような状態の時に条件を満たすか考えてみる
1: ai = i and aj = j
2: ai = j and aj = i

1は競技中に自分が考えていたものと同じ。つまりi==aiとなっているものの数を数える
そこから2つを選ぶ組み合わせの数になるよね

2が気づけなかった。
iが一つの通りになればjは固定される分けだからiのループで十分だよねっていう話か
"""

N = int(input())
A = list(map(int, input().split()))

ans = 0

# まず1のパターン
n = 0
for i, x in enumerate(A):
    if i+1 == x:
        n += 1

# 添字と値が同じになっているものから2個組み合わせ
ans += (n * (n-1) // 2)

# パターン2の探索
for i, j in enumerate(A):
    if i+1 < j and A[j-1] == i+1:
        ans += 1
print(ans)
