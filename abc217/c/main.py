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
import array

# 全てのi に対してQのpi番目の要素がiである
N = int(input())
P = list(map(int, input().split()))
ans = [-1 for _ in range(N)]

for i in range(N):
    cur = P[i]
    ans[cur-1] = i+1
print(*ans)
