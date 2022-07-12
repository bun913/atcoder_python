# -*- coding: utf-8 -*-
"""
Nが最大で10 **5
1から順にAのindex番号+1を出力してやれば良いだけだが、毎回Aのリストを探すのは遅い
Aの順とindex番号を辞書化しておいてやればよいだけかな
"""

N = int(input())
A = list(map(int, input().split()))

memo = dict([(A[i], i+1) for i in range(N)])


ans = []

for i in range(N):
    key = i + 1
    ans.append(memo[key])

print(*ans)
