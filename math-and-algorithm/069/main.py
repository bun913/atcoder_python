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
# まず考えつくのがx,yをそれぞれ数え上げる方法
# ただこれだと、xのループだけでも10**18かかってしまう
# 今回求める必要があるのは,xとyを掛け合わせた最大値のみ
a, b, c, d = list(map(int, input().split()))
# 全ての組み合わせの中から最大値を求めれば良い
# (a, c) (a, d), (b,c), (b,d)
ans = max(a*c, a*d, b*c, b*d)
print(ans)
