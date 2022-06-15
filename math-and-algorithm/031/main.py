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
N = int(input())
A = list(map(int, input().split()))
dp1 = [0 for _ in range(N+1)]
dp2 = [0 for _ in range(N+1)]
# dp1をi日目に勉強した場合の最適値
# dp2をi日目に勉強しなかった場合の最適値を保持するリストとする

for i in range(1, N+1):
    # 勉強しなかった場合
    no = max(dp1[i-1], dp2[i-1])
    # 勉強した場合
    study = dp2[i-1] + A[i-1]
    dp1[i] = study
    dp2[i] = no
# print(dp1)
# print(dp2)
print(max(dp1[-1], dp2[-1]))
