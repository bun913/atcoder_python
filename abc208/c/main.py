"""
N人の国民
K個のお菓子を持って持っているお菓子がなくなるまで国民にお菓子を配る
- N個以上の場合は全員に1個ずつおかしを配る
- その時点で持っているお菓子をKDとして国民番号が小さい方から1個ずつ配る
i人目の国民はなんこのお菓子を持っているか

単純にまずNで割れる数を数えて、全員に配る
そこからのあまりを出す(KD)
もし自分の番号が前から数えてKDいないだったら+1した数を与えればよいだけでは
"""
from bisect import bisect_left

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
base = K // N
ind_list = []
AD = sorted(A)

for a in A:
    i = bisect_left(AD, a)
    ind_list.append(i)


KD = K % N
for i in range(N):
    ind = ind_list[i]
    ans = base
    if ind <= KD-1:
        ans += 1
    print(ans)
