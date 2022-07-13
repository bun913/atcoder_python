# -*- coding: utf-8 -*-
"""
数xi がki回目に登場するのはAの前から何番目の要素をみた時かを出力

普通に考えれば2重ループで検索すれば良いが,Nが2 * 10**5 なので間に合わない
まぁでもあらかじめaの数がそれぞれ何回、何番目に登場したかメモしておけば良いというだけ
どういう持ち方をするか {1: set(1番目, 4番目, 5番目)}とすれば辞書を引くのも1,setから要素を見つけるのも計算量1でいけそう
"""

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))

# 各数字が出現した回数をメモ
displaeyd_memo = dict([(a, 0) for a in A])
# 各数字の出現回数と位置をメモ
memo = dict([(a, {}) for a in A])
for i in range(N):
    cnt = i + 1
    a = A[i]
    dic = memo[a]
    k = displaeyd_memo[a] + 1
    dic[k] = cnt
    displaeyd_memo[a] += 1

for q in range(Q):
    x, k = list(map(int, input().split()))
    # memoに要素が存在しない
    if x not in memo:
        print(-1)
        continue
    d = memo[x]
    # 要素があるけどK個要素がない
    if k not in d:
        print(-1)
        continue
    ans = d[k]
    print(ans)
