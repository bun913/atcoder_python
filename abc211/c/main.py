"""
このうち8文字を選んで、左から順にchokudaiとする方法の全通り数
Sが10**5なのでcombinationsとかは無理
DPでi文字めまでを使ってchokudaiのk文字目までを作る方法が何通りあるか
"""
S = input()
N = len(S)
S = "?" + S
T = "?chokudai"
# 表を作成する
dp = [[0 for _ in range(9)] for _ in range(N + 1)]
mod = 10**9 + 7
# 初期化(すぐにわかるところを埋める)
for i in range(N + 1):
    dp[i][0] = 1
# 表の小さい方から答えに辿り着くまで埋める
for i in range(1, N + 1):
    for k in range(1, 9):
        if S[i] == T[k]:
            dp[i][k] = dp[i - 1][k] + dp[i][k - 1]
        else:
            dp[i][k] = dp[i - 1][k]
        dp[i][k] %= mod
print(dp[-1][-1])
