# -*- coding: utf-8 -*-
"""
めぐる式二部探索で組み直したバージョン
今回はxj以上のもので、最小のindexの値が分かれば良い
なので、okの条件をx以上としたうえで、条件を満たす最小のindexを取れば良い

※他にもいくつかアプローチが考えられそうで、例えばxより大きいをOKとして
最終的に出力されるNGを使うというてこともできそう
"""

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
AD = sorted(A)


def is_ok(x: int, v):
    if v >= x:
        return True
    return False


def meguru_bisect(ng, ok, x):
    '''
    今回はx以上のものをOKとして使う
    そうすればOKがx以上のものの一番左側となるため、x以上となる最初のindexがわかる
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(x, AD[mid]):
            ok = mid
        else:
            ng = mid
    return ok


for j in range(Q):
    x = int(input())
    i = meguru_bisect(-1, len(AD), x)
    ans = N - i
    print(ans)
