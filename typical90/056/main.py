# -*- coding: utf-8 -*-
"""
N日間A,かBを必ず購入する
ちょうどS円になるように購入したい
Nが100なのでbit全探索は無理

DPでいけそう。横軸の最大値をSとして2パターンを考えていく
"""


def main():
    n, s = map(int, input().split())
    dp = [[0]*(s+1) for _ in range(n+1)]
    dp[0][0] = 1
    ab = []
    for i in range(n):
        a, b = map(int, input().split())
        ab.append((a, b))
        for j in range(s+1):
            if dp[i][j]:
                if j+a <= s:
                    dp[i+1][j+a] = 1
                if j+b <= s:
                    dp[i+1][j+b] = 1
    if dp[n][s] == 0:
        print('Impossible')
        exit()
    tate = n
    yoko = s
    ans = ''
    while tate > 0:
        a, b = ab[tate-1]
        if yoko-a >= 0 and dp[tate-1][yoko-a]:
            ans += 'A'
            yoko -= a
        else:
            ans += 'B'
            yoko -= b
        tate -= 1
    print(ans[::-1])


main()
