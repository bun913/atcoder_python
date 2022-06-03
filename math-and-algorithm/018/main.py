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
from itertools import combinations

n = int(input())
l = list(map(int, input().split(" ")))

# nから2個を選び出す組み合わせを全て列挙
# これだと Combi nの2 となりタイムアウトになってしまう
# 列挙に n**2かかるので
# combi_list = combinations(range(0, len(l)), 2)
# ans = 0
# for a, b in combi_list:
#     pa = l[a]
#     pb = l[b]
#     if pa + pb == 500:
#         ans += 1
# print(ans)

# よく問題をみると aは100,200,300,400のいずれかしかないことがわかる
# 500の組み合わせになるのは (100,400) と (200,300)しかない
# これを積の法則を利用すれば簡単に求めれる
count_100_ = l.count(100)
count_200_ = l.count(200)
count_300_ = l.count(300)
count_400_ = l.count(400)
ans = (count_100_ * count_400_) + (count_200_ * count_300_)
print(ans)
