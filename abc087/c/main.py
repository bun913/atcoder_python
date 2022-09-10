"""
各マスにおける最高の値をDPでメモしていく

マスの探し方は深さ優先探索でqueを使う
"""
from collections import deque

N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]
DP = [[0 for j in range(N)] for _ in range(2)]
q = deque([(0, 0)])

while len(q) > 0:
    cur = q.popleft()
    x = cur[0]
    y = cur[1]
    # 現在のマスの最大値をメモ
    point = A[x][y]
    bef_point = 0
    if x - 1 >= 0:
        bef_point = max(bef_point, DP[x - 1][y])
    if y - 1 >= 0:
        bef_point = max(bef_point, DP[x][y - 1])
    DP[x][y] = point + bef_point
    # 次のターゲットがあればキューに入れる
    if x + 1 <= 1:
        q.appendleft((x + 1, y))
    if y + 1 <= N - 1:
        q.appendleft((x, y + 1))
print(DP[-1][-1])
