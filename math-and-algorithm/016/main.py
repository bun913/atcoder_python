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
n = int(input())
l = list(map(int, input().split(" ")))


def gcd(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return max(a, b)
    big = max(a, b)
    small = min(a, b)
    mod = big % small
    return gcd(mod, small)


# 順番はどうでも良いのでスタックっぽく出し入れを行う
while True:
    if len(l) <= 1:
        print(l[0])
        exit()
    a = l.pop()
    b = l.pop()
    g = gcd(a, b)
    l.append(g)
