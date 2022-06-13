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
ans = set([i for i in range(1, 1001)])
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(N):
    a = A[i]
    b = B[i]
    s = set()
    for j in range(a, b+1):
        s.add(j)
    ans = ans.intersection(s)
print(len(ans))
