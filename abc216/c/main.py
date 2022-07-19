"""
合計120回いないの魔法で箱の中のボールの数をちょうどN個にする方法
最初はAをするしかない

Nを逆から見ていて、2で割れるならBをする。
そうではないならAの処理をしてやる。
というふうにNをどんどん小さくしていく
"""

N = int(input())
cur = N
ans = []
while not cur == 0:
    if cur % 2 == 0:
        cur = cur // 2
        ans.append('B')
        continue
    cur -= 1
    ans.append('A')
print(''.join(ans[::-1]))
