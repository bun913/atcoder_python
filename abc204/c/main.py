"""
道路Aiを通ると都市AiからBiの通行ができる
一方通行
スタート地点からゴール地点の年の組の総数
幅優先探索
"""
from collections import deque

# 経路情報を二次元配列として受け取り
N, M = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = list(map(int, input().split()))
    graph[a].append(b)


# 幅優先探索でスタート
def bfs(start: int) -> int:
    cnt = 1
    # 訪問済みの歳を管理
    visited = [False for _ in range(N + 1)]
    visited[start] = True
    que = deque()
    que.append(start)
    while que:
        cur = que.popleft()
        for to in graph[cur]:
            if visited[to] is False:
                cnt += 1
                visited[to] = True
                que.append(to)
    return cnt


ans = 0
for x in range(1, N + 1):
    ans += bfs(x)
print(ans)
