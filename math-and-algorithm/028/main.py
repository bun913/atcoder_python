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

"""
動的計画法の基本的な問題
問題を小さく、かつ分割して考えようということ
今回で言えばいきなりn段目のことを考えるのではなく、各段の最小のステップを求めて次のステップの最小値を求める
前の結果を使うのでまさに漸化式の考え方になるかな
"""

n = int(input())
l = list(map(int, input().split()))
dp_list = []

for i in range(n):
    if i == 0:
        dp_list.append(0)
    elif i == 1:
        dp_list.append(abs(l[1] - l[0]))
    else:
        step1 = abs(l[i] - l[i-1]) + dp_list[i-1]
        step2 = abs(l[i] - l[i-2]) + dp_list[i-2]
        dp_list.append(min([step1, step2]))
print(dp_list[-1])
