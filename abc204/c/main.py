"""
道路Aiを通ると都市AiからBiの通行ができる
一方通行
スタート地点からゴール地点の年の組の総数
幅優先探索
"""
from collections import deque

N, M = list(map(int, input().split()))
connects = [[] for _ in range(N + 1)]

# 経路を二次元配列にメモ
for _ in range(M):
    A, B = list(map(int, input().split()))
    connects[A].append(B)

# 幅優先探索の実装
def bfs(start: int) -> int:
    cnt = 1
    # 次の点を格納するキュー
    q = deque([start])
    # 訪問済みの都市を格納する
    visited = [False for _ in range(N + 1)]
    visited[start] = True
    while q:
        # 現在地点をfromとする
        fr = q.popleft()
        # frが持っている経路をforで回す
        for to in connects[fr]:
            if visited[to] is False:
                cnt += 1
                visited[to] = True
                q.append(to)
    return cnt


ans = 0
for i in range(1, N + 1):
    ans += bfs(i)
print(ans)
