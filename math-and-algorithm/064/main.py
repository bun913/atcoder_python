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
# もしありうる値を全て全探索しようとした場合
# k,nが最大50
# 数を一つ選ぶのに50
# それを50回(k回)繰り返す
# それをN回なので
# (2**n)**k
# 無理

# そこで偶数奇数に着目する
# やる操作はあくまで+1, -1を加算するだけ
# それをK回繰り返すというだけ
# また操作を繰り返すことで、偶数->奇数と繰り返していくだけ
# 1:だからまず、配列の総和の偶数奇数がKの偶数奇数とあってないとだめ
# 2:次に配列の総和が Kを上回っていたらアウト
# これを満たしていれば、最初に全てのAの値を0にして、あとは適当に+1,-1を繰り返せばなんでも0にできる

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

s = sum(A)
# 1の条件
if s % 2 != K % 2:
    print('No')
    exit()
# 2の条件
if s > K:
    print('No')
    exit()
print('Yes')
