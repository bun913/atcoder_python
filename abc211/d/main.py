"""
"""
from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

q = deque([1])
inf = 10 ** 15
time = [inf] * (N+1)
time[1] = 0
counter = [0] * (N+1)
counter[1] = 1

# 幅優先探索を行いながら最短経路と経路数をカウントする
while q:
    cur = q.popleft()
    for nex in G[cur]:
        if time[nex] == inf:
            # もし行ける都市の移動時間が更新されていなければ更新
            time[nex] = time[cur] + 1
            # 経路数は今いる都市の経路数と同じ
            counter[nex] = counter[cur]
            q.append(nex)
        else:
            # 移動時間が更新済みなら
            # 今いる年から+1の時間でいける年の場合は経路数をたす
            if time[nex] == time[cur] + 1:
                counter[nex] += counter[cur]
                counter[nex] %= 10**9 + 7
if time[N] == inf:
    print(0)
    exit()
print(counter[N])
