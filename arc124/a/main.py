# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from functools import reduce
from itertools import combinations
import math

# 同じカードの枠に制約がつくことはない
N, K = list(map(int, input().split()))
# 残りの枠の個数を保持
frames = [K for _ in range(N)]


def decre(n: int):
    if n > 1:
        return n-1
    else:
        return n


for i in range(1, K+1):
    c, k = list(map(str, input().split()))
    k = int(k)
    left = []
    right = []
    middle = [1]
    # print('frames:', frames)
    if c == 'L':
        left = list(map(decre, frames[:k-1]))
        right = frames[k:]
    else:
        left = frames[:-k]
        right = list(map(decre, frames[-k+1:]))
    print('---------------------------')
    print('条件: {}から{}番目が{}'.format(c, k, i))
    print('frameの長さ:{}'.format(len(frames)))
    print('fram:{}'.format((frames)))
    print('left:{}'.format(left))
    print('midl:{}'.format(middle))
    print('righ:{}'.format(right))
    frames = left + middle + right
    print('afte:{}'.format(frames))
# 最後にあまりを求めるととんでもない数になる
mod = reduce(lambda total, current: total * (current % 998244353), frames, 1)
ans = mod % 998244353
print(ans)
