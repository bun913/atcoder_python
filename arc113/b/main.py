# -*- coding: utf-8 -*-
"""
まずBとCだけ計算してAを何回階乗するかということを求めるか

1の位だけ見てやれば良いAの1のくらいは1~9
1~9の規則性をあらかじめメモしておけば良いのでは
"""
A, B, C = list(map(int, input().split()))
period_memo = dict([(i, []) for i in range(1, 10)])
# 1~9の階乗した結果の1のくらいの規則性をメモ
for i in range(1, 10):
    for j in range(1, 11):
        s = str(pow(i, j))
        about1 = int(s[-1])
        if about1 in period_memo[i]:
            break
        period_memo[i].append(about1)
a_about1 = int(str(A)[-1])
if a_about1 == 0:
    print(0)
    exit()
mod = len(period_memo[a_about1])
period = pow(B, C, mod)
ans = period_memo[a_about1][period - 1]
print(ans)
