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
l = list(map(int, input().split()))
k = int(input())
sorted_l = sorted(l, reverse=True)
for _i in range(k):
    _max = sorted_l[0]
    sorted_l[0] = _max * 2
print(sum(sorted_l))