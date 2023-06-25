"""
Nが10**5なので、普通にi,jを全て探索すると間に合わない
式を一般化しておけばかなり楽に計算できる
実際に計算してみると式を一般化できることに気づく
"""
N = int(input())
A = list(map(int, input().split()))
ans = 0
MOD = 10**9 + 7
s = sum(A)
s -= A[0]

for i in range(N-1):
    cnt = A[i] * s % MOD
    ans += cnt
    s -= A[i+1]
print(ans % MOD)
