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
from itertools import permutations

S, K = input().split()
K = int(K)

cands = list(permutations(S, len(S)))
cands_to_s = [''.join(t) for t in cands]
cands_to_s = list(set(cands_to_s))
_sorted = sorted(cands_to_s)
print(_sorted[K-1])
