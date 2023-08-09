"""
数列の一部を取り出して話をとった場合、作れる数は何か？
というものを部分和問題というらしい
部分和問題はDPで解ける
今回は2つのオーブンを使うわけだが、1つのオーブンで作れる料理がわかれば片方のオーブンで作れる料理もわかる
DPでオーブンAに割り振る料理を求めていく
"""
from functools import reduce

N = int(input())
T = list(map(int, input().split()))
limit = sum(T)
dp = [[False for _ in range(limit+1)]  for _ in range(N+1) ]
dp[0][0] = True

for i in range(1, N+1):
    cur = T[i-1]
    for j in range(limit+1):
        if dp[i-1][j] is True:
            dp[i][j] = True
            continue
        # jがi番目の料理を明らかに作れない場合はスキップ
        if j < cur:
            continue
        if dp[i-1][j-cur]  is True:
            dp[i][j] = True
            continue

# dp[N]というのがTの全ての料理を組み合わせて作れる数のリストになっている
# つまり全ての料理の組み合わせで作れる和のパターンになってる
# このパターンの中から最小のものを探せばoK
ans = 10**15
sum_t = sum(T)
for K in range(limit+1):
    # N番目までの数を組み合わせてKを作れるか
    if dp[N][K] is True:
        oven1 = K
        oven2 = sum_t - K
        ans = min(ans, max(oven1, oven2))
print(ans)
