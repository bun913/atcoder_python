"""
N個の町のテレポーター
K回使うとどの街に到着するか
ループに辿り着くまでのステップ数と
ループの周期がわかれば良い
"""
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 2回目に訪れた街とステップ数を記録する
visited = [-1] * N
step = 0
nex = 0
while True:
    if visited[nex] != -1:
        break
    visited[nex] = step
    nex = A[nex] - 1
    step += 1
    # ループに入る前に終了する場合
    if step == K:
        print(nex + 1)
        exit()

until_loop_step = visited[nex]
loop_period = step - until_loop_step

# ループに入ってから終了する場合
k = (K - until_loop_step) % loop_period
for i in range(N):
    if visited[i] == until_loop_step + k:
        print(i + 1)
        exit()
