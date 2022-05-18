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

A, B, W = list(map(int, input().split()))
# 数え上げでありえる最大個数
_max = 1000 * W
# A*個数 ~ B*個数ならこの範囲は全て作れるはず
# だって重さは小数点刻みで良いんだから、みかんを少しだけづつ大きくすれば
# 理論上全ての数が作れるはず！！
ans_min = float('inf')
ans_max = 0

# みかんの個数を1個から1000*W(グラムに直している)まで試す
for i in range(1, 1000*W+1):
    if i*A <= 1000*W <= i*B:
        ans_max = i
        if i < ans_min:
            ans_min = i
if ans_max == 0:
    print('UNSATISFIABLE')
else:
    print("{} {}".format(ans_min, ans_max))
