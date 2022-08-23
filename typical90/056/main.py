# -*- coding: utf-8 -*-
"""
N日間A,かBを必ず購入する
ちょうどS円になるように購入したい
Nが100なのでbit全探索は無理

DPでいけそう。横軸の最大値をSとして2パターンを考えていく
"""
N, S = list(map(int, input().split()))
DP = [[False for _ in range(S+1)] for _ in range(N)]
AB = []

for i in range(N):
    A, B = list(map(int, input().split()))
    AB.append((A, B))
    for j in range(S+1):
        # 最初の行のメモ
        if i == 0:
            DP[i][A] = True
            DP[i][B] = True
            break
        # 上の行で商品を足せていないマスは飛ばす
        if DP[i-1][j] is False:
            continue
        # 今のA・Bを足した金額がS以下ならTrueと記憶する
        if j + A <= S:
            DP[i][j+A] = True
        if j + B <= S:
            DP[i][j+B] = True
if DP[-1][-1] is False:
    print('Impossible')
    exit()
# DPを下から見て、答えを復元する必要がある
ans = []
cur = S
for i in range(N-1, 0, -1):
    A, B = AB[i]
    if DP[i-1][cur-A] is True:
        cur -= A
        ans.append('A')
        continue
    if DP[i-1][cur-B] is True:
        cur -= B
        ans.append('B')
        continue
if cur == AB[0][0]:
    ans.append('A')
else:
    ans.append('B')
print(*reversed(ans), sep='')
