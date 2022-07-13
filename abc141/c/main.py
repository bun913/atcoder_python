# -*- coding: utf-8 -*-
"""
解答前のメモ

正解した人以外の点が減るというのがポイント
辞書とかでそれぞれのポイントを持って、それを減らしていけば
毎回最大で10**5の繰り返しが入るので間に合わない。

まぁ、でも実際にポイントを減らしていく必要はなく
単純に自分いがいの奴が何回正解したかがわかれば良いだけ
(Q-自分の正解数)が減点される数字
なので、それをKから引いて0以下ならNoと、逆ならYesと出すだけだろうと思う
"""

N, K, Q = list(map(int, input().split()))
correct_ans_dic = dict([(i, 0) for i in range(N)])

for i in range(Q):
    a = int(input())
    correct_ans_dic[a-1] += 1

for i in range(N):
    own_correnct_ans = correct_ans_dic[i]
    decrese_point = (Q-own_correnct_ans)
    if max(0, K-decrese_point) == 0:
        print('No')
        continue
    print('Yes')
