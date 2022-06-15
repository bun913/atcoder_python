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
first_win = True
for i in range(60):
    if N == (2**i) - 1:
        first_win = False
        break
    if N < (2**i) - 1:
        break
if first_win is True:
    print('First')
else:
    print('Second')
