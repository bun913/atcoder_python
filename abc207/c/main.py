"""
N個の区間
1ならX以上Y以下の全ての実数からなる区間
2ならX以上Y未満
3ならXより大きくY以下
4ならXより大きくY未満
N以下の整数の組(i,j)が共通部分を持つ数
"""
N = int(input())
dists = []

for _ in range(N):
    t, l, r = list(map(int, input().split()))
    # 1の状態
    dist = [l, r]
    if t == 2 or t == 4:
        dist[1] -= 0.5
    if t == 3 or t == 4:
        dist[0] += 0.5
    dists.append(dist)

# 総当たりで共通の個数を求める
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        a = dists[i]
        b = dists[j]
        maxl = max(a[0], b[0])
        minr = min(a[1], b[1])
        is_count_up = not minr < maxl
        ans += max(a[0], b[0]) <= min(a[1], b[1])
print(ans)
