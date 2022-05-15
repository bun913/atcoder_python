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
a_list = [ int(input()) for _ in range(N)]
ans = -1
count = 0
i = 1
# ボタンの回数以上にループを繰り返す必要がない
for _ in range(N):
    if i == 2:
        print(count)
        exit()
    i = a_list[i-1]
    count += 1
print(ans)