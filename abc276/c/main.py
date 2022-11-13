# -*- coding: utf-8 -*-
"""
解く前のメモ用
辞書順で並べた時PがK番目である
K-1番目の順列を求める

Nが100だからbit全探索は無理
"""
from collections import deque

N = int(input())
P = list(map(int, input().split()))

usable = []
rest = deque(P)

# 末尾を消してストックに追加。取り出した数より小さい数があったら終わり
while True:
    p = rest.pop()
    usable.append(p)
    if sorted(usable)[0] < p:
        break
# usableの最後の要素より小さい中で最も大きい数をおく
a = sorted(filter(lambda x: x < usable[-1], usable))[-1]
rest.append(a)
usable.remove(a)
# 後は大きい順に配置するだけ
print(*rest, *sorted(usable, reverse=True))
