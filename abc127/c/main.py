# -*- coding: utf-8 -*-
"""
解く前のメモ

N枚のIDカードとM個のゲート
i番目のゲートは、Li,Li+1,Ri番目のIDカードのうちどれか1枚で通過できる

条件がよく分からん
要するに今i番目としてi+n(n<=1)以上にでてくる全てのL,Rで開けられるということ？

しばらく悩んでやっとわかった
Li 以上 Ri以下のカードでも開けられるということかな

困ったことにNが10**5なので、L..Rのところで二重ループしてたら間に合わない
Lの最大値とRの最小値が分かればその間の数が答えになりそう
"""

N, M = list(map(int, input().split()))
l_max = -1
r_min = 10 ** 5 + 3

for i in range(M):
    l, r = list(map(int, input().split()))
    l_max = max(l_max, l)
    r_min = min(r_min, r)

ans = r_min - l_max + 1
ans = max(0, ans)
print(ans)
