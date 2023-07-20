from collections import deque

N, M = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = list(map(int, input().split()))
    G[a-1].append(b-1)

ans = 0
for start in range(N):
    q = deque([start])
    visited = [False] * N
    visited[start] = True
    while q:
        cur = q.popleft()
        for nex in G[cur]:
            if visited[nex] is True:
                continue
            visited[nex] = True
            q.append(nex)
    ans += sum(visited)
print(ans)
