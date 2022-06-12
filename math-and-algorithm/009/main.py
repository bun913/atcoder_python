"""
Atcoderの問題解く用

1行1列データ

#str型で受け取るとき
s = input() 
#int型で受け取るとき
s = int(input()) 
#float型　(小数)で受け取るとき
s = float(input())

(1,N)行列データ
s = input().split()
# listで整数で受け取る
l = list(map(int, input().split()))

その他
https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785
"""
N, S = list(map(int, input().split()))
A = list(map(int, input().split()))
# DPで解くため1行あたり10,000までの値を持つ二次元配列を用意
limit = S+1
dp = [[None] * (S + 1) for i in range(N + 1)]
dp[0][0] = True

# 数字がvになるような値が作れるか作れないか見れば良いだけ
# 今引いているカードが
for i in range(1, N+1):
    for j in range(0, limit):
        now = A[i-1]
        # 現在のカードを使えない時(vが現在引いているカードの値より低い)
        if j < now:
            dp[i][j] = dp[i-1][j]
        else:
            no_use = dp[i-1][j]
            use = dp[i-1][j-now]
            if no_use is True or use is True:
                dp[i][j] = True
            else:
                dp[i][j] = False
ans = 'No'
if dp[N][S] is True:
    ans = 'Yes'
print(ans)
