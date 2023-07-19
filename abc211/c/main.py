"""
chokudaiという部分文字列を何個作れるか
部分文字列DPの考え方を使う
"""
S = input()
L = list(S)
S = '?' + S  # 適当に最初の文字を埋めておく
T = '?chokudai'
mod = 10**9 + 7

dp = [[0] * 9 for _ in range(len(S))]
# すぐにわかるところを埋める
for i in range(len(S)):
    dp[i][0] = 1

for i in range(1, len(S)):
    for j in range(1, 9):
        # 今見ている文字が作りたい文字と同じ場合
        if S[i] == T[j]:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        else:
            # 同じ文字じゃない場合これまでの結果を使うしかない
            dp[i][j] = dp[i-1][j]
        dp[i][j] %= mod
print(dp[-1][-1])
