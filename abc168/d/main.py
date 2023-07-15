"""
部屋にある道標を見てそれが指す部屋に移動する
部屋1に最小の移動回数でたどり着くように道標を配置する
経路を記録しておけば良い
"""
from collections import deque

# 入力の受け取り
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

dist = [-1] * N
dist[0] = 0
prev_routes = [0] * N
q = deque([0])

while q:
    cur = q.popleft()
    for nex in G[cur]:
        # 訪問済みならスキップ
        if dist[nex] != -1:
            continue
        dist[nex] = dist[cur] + 1
        prev_routes[nex] = cur
        q.append(nex)
# 部屋1にたどり着けない場合
for min_dist in dist:
    if min_dist == -1:
        print("No")
        exit()

# 最小距離の出力
print("Yes")
for i, prev_route in enumerate(prev_routes):
    if i == 0:
        continue
    print(prev_route + 1)
