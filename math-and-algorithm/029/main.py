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
dp_list = []
for i in range(n):
    if i == 0:
        dp_list.append(1)
        continue
    if i == 1:
        dp_list.append(2)
        continue
    else:
        v1 = dp_list[i-1]
        v2 = dp_list[i-2]
        dp_list.append(v1+v2)
print(dp_list[-1])
