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
from decimal import Decimal

A, B, C = list(map(int, input().split()))

if C % 2 == 0:
    aba = abs(A)
    abb = abs(B)
    if aba == abb:
        print('=')
    elif aba > abb:
        print('>')
    else:
        print('<')
else:
    if A < B:
        print('<')
    elif A > B:
        print('>')
    else:
        print('=')
