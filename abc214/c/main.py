"""
動的計画法というか漸化式のような形で自分より一個前の人が
最短で宝石をもらう時間を求め続ければOKでは
"""
N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

# ただし最初に宝石をもらうタイミングを考える必要があるので
# 2周して考える

dp = [float('inf')] * N
for i in range(2*N):
    idx = i % N
    prev_idx = (i-1) % N
    # まだ前の人の情報が確定していない場合は一旦仮の値を入れる
    if prev_idx == float('inf'):
        dp[idx] = T[idx]
        continue
    cand1 = T[idx]
    cand2 = dp[prev_idx] + S[prev_idx]
    dp[idx] = min(cand1, cand2)

for ans in dp:
    print(ans)
