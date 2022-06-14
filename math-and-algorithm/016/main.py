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


def gcd(i: int, j: int) -> int:
    _max = max(i, j)
    _min = min(i, j)
    if _min == 0:
        return _max
    else:
        return gcd(_min, _max % _min)


N = int(input())
A = list(map(int, input().split()))
n = A[0]
for i in range(1, len(A)):
    _next = A[i]
    n = gcd(n, _next)
print(n)
