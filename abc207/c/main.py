"""
全部の区間をl以上、r以下という形で持ち直す
2重ループで区間を全探索する
その区間について、lとrの大小関係によって場合分けをする
"""
N = int(input())
tlr = [list(map(int, input().split())) for _ in range(N)]
intervals = []

for t, l, r in tlr:
    left = l
    right = r
    if t == 2:
        right -= 0.5
    if t == 3:
        left += 0.5
    if t == 4:
        left += 0.5
        right -= 0.5
    intervals.append((left, right))

# 全探索で答えを求める
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        left_i, right_i = intervals[i]
        left_j, right_j = intervals[j]
        if right_i < left_j:
            continue
        if right_j < left_i:
            continue
        ans += 1
print(ans)
