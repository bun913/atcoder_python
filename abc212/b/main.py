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
s = input()
# 1種類
if len(set(s)) == 1:
    print("Weak")
    exit()
step = True
for i in range(3):
    now = int(s[i])
    _next = int(s[i+1])
    if (now + 1) % 10 != _next:
        step = False
if step:
    print("Weak")
else:
    print("Strong")
