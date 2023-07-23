"""
"""
import heapq
import sys

sys.setrecursionlimit(10**8)

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

# 小さい順に回るためソートする（これでnexが小さい順になる）
for i in range(N):
    G[i].sort()

routes = []


def dfs(now, pre):
    routes.append(now+1)
    for to in G[now]:
        if to == pre:
            continue
        # さらに先に行く
        dfs(to, now)
        # これは今のところに戻ってきたので、ルートに戻ってきたことを記録する
        routes.append(now+1)


dfs(0, -1)
print(*routes)
