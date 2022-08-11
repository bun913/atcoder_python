# -*- coding: utf-8 -*-
"""
解く前のメモ

まさに区間和で俺に累積和を使えと言われているような気がする
1組と2組の累積和を出しておけばN1の計算量で行ける
"""
# 入力から各クラスの点数を配列にセットする
N = int(input())
p1 = []
p2 = []

# 学籍番号という要素が邪魔なのでいないところには0としてマークをする(Nullとしたいけど累積和で邪魔)
for i in range(N):
    cl, score = list(map(int, input().split()))
    if cl == 1:
        p1.append(score)
        p2.append(0)
        continue
    p2.append(score)
    p1.append(0)
# クラスの点数の累積和を配列で用意
# pythonはitertools accumrateで簡単に累積和を作れるが練習のため一旦手動で作成する
s1 = [0 for _ in range(N)]
s2 = [0 for _ in range(N)]
for i in range(N):
    score = p1[i]
    s1[i] = s1[i-1] + score if i != 0 else score
for i in range(N):
    score = p2[i]
    s2[i] = s2[i-1] + score if i != 0 else score
# 累積和の最初の要素として0を挿入
s1.insert(0, 0)
s2.insert(0, 0)

Q = int(input())
for _ in range(Q):
    left, right = list(map(int, input().split()))
    left -= 1
    print(s1[right] - s1[left], s2[right] - s2[left])
