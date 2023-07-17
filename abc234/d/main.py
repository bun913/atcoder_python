"""
Pの数列をどんどん更新していきK番目に大きい値を出力する
要素数をKとするヒープキューを使って、Pの数列をどんどん更新していく
"""
import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))

# 要素数をKとするヒープキューを作成
q = P[:K]
heapq.heapify(q)
# K番目に大きい値を出力する
for i in range(K-1, N):
    if i == K-1:
        print(q[0])
        continue
    p = P[i]
    min_val = heapq.heappop(q)
    if p > min_val:
        heapq.heappush(q, p)
    else:
        heapq.heappush(q, min_val)
    print(q[0])
