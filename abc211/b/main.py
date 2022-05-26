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
l = [input() for _ in range(4)]
is_h = l.count("H") == 1
is_2h = l.count("2B") == 1
is_3h = l.count("3B") == 1
is_hr = l.count("HR") == 1
is_all = all([is_h, is_2h, is_3h, is_hr])

ans = "No"
if is_all:
    ans = "Yes"
print(ans)
