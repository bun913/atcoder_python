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


def is_prime_number(n: int) -> bool:
    for i in range(2, n+1):
        if n % i == 0 and i != n:
            return False
    return True


n = int(input())
ans = []
for i in range(2, n+1):
    is_prime = is_prime_number(i)
    if is_prime:
        ans.append(str(i))
print(" ".join(ans))
