# -*- coding: utf-8 -*-
"""
1件計算でなんとかできそうだがXが10**18と非常に大きい
LUやRUは移動していないのと同じでるので入力から無駄な部分を消す
"""

N, X = map(int, input().split())
S = input()
memo = []

for s in S:
    if len(memo) == 0:
        memo.append(s)
        continue
    if s == 'L' or s == 'R':
        memo.append(s)
        continue
    # sがU確定
    if memo[-1] == 'L' or memo[-1] == 'R':
        memo.pop()
        continue
    if memo[-1] == 'U':
        memo.append(s)
        continue

ans = X
for s in memo:
    if s == "L":
        ans *= 2
        continue
    if s == "R":
        ans *= 2
        ans += 1
        continue
    ans //= 2
print(ans)
