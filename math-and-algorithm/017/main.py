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
import copy


def gcd(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return max(a, b)
    big = max(a, b)
    small = min(a, b)
    mod = big % small
    return gcd(mod, small)


def mcl(a: int, b: int) -> int:
    g = gcd(a, b)
    ans = g * (a // g) * (b // g)
    return ans


n = int(input())
l = list(map(int, input().split(" ")))

ans = 1
while True:
    if len(l) == 1:
        break
    a = l.pop()
    b = l.pop()
    m = mcl(a, b)
    l.append(m)

print(l[0])
