# -*- coding: utf-8 -*-
"""
解く前のメモ

Nが10**5まであるので、とても全部をforで回すのは無理だよねという話
AとBが決まればCは二部探索で・・・みたいなことも厳しい
選び方の総数というのがポイントな気がする

以下解説を見て分かった回答方法
46の倍数になる組み合わせというのがポイント
46の倍数になるということは各配列を46で割ったあまりを求める
とすれば、0の数,1の数...45の数と求められる
あとは足して46となるように全ての組み合わせを全探索すれば良いだけ
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ad = list(map(lambda n: n % 46, A))
bd = list(map(lambda n: n % 46, B))
cd = list(map(lambda n: n % 46, C))

a_counts = [ad.count(n) for n in range(46)]
b_counts = [bd.count(n) for n in range(46)]
c_counts = [cd.count(n) for n in range(46)]

ans = 0
for a in range(46):
    for b in range(46):
        for c in range(46):
            if (a+b+c) % 46 == 0:
                a_cnt = a_counts[a]
                b_cnt = b_counts[b]
                c_cnt = c_counts[c]
                ans += a_cnt * b_cnt * c_cnt
print(ans)
