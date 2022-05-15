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
A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0

for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            s = (500 * a) + (100 * b) + (50*c)
            if X == s:
                ans += 1
print(ans)
