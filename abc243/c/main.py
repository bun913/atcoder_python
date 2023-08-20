# -*- coding: utf-8 -*-
"""
人同士でぶつかる人がいるか調べる
ぶつかる人の条件をわけて考える
- y軸が同じ人がいるか（これがないと絶対にない）
- x軸とSが以下のパターン
    - 

データをどのように持つか{y軸: [x軸, S]}

制約
- Nが2*10**5
- 与えられる(x,y)は全て異なる
"""
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
S = list(input())

# 各数字のLの最下限のx座標と、Rの最下限のx座標を持つ
# {y軸: {L: x座標, R: x座標}}
memo = {}
for i in range(N):
    x, y = XY[i]
    s = S[i]
    if y not in memo:
        memo[y] = {}
    if s not in memo[y]:
        memo[y][s] = x
    else:
        if s == "R":
            memo[y][s] = min(memo[y][s], x)
        else:
            memo[y][s] = max(memo[y][s], x)
for v in memo.values():
    if "L" not in v:
        continue
    if "R" not in v:
        continue
    if v["R"] < v["L"]:
        print("Yes")
        exit()
print("No")
