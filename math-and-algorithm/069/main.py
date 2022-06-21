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
a, b, c, d = list(map(int, input().split()))
# 全てのパターンを考えるだけで良い
# マイナスの数を考慮するとifがめんどくさくなる
# 単純にあり得るパターンはa,b,c,dそれぞれの端っこだけ
# a*c, a*d, b*c, b*dの最大値を取る

ans = max(a*c, a*d, b*c, b*d)
print(ans)
