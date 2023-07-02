N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

rest = K
# 各街に到達した回数を保持する配列
visited = [-1] * N
now_cnt = 0
iter_cnt = 0
pos = 0
while True:
    # ループより先に到達する場合
    if rest == 0:
        print(pos + 1)
        exit()
    # まだ未到達だった場合
    if visited[pos] == -1:
        visited[pos] = now_cnt
        now_cnt += 1
        rest -= 1
        pos = A[pos] - 1
        continue
    # 2回目の到達の場合
    iter_cnt = now_cnt - visited[pos]
    break
rest %= iter_cnt
for i in range(N):
    # 現在のポジションからrest回移動したポジションとひとしければ、その街が答え
    if visited[i] == visited[pos] + rest:
        print(i + 1)
        exit()
