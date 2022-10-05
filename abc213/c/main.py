"""
Nは最低でも10**5ある
数の書かれたカードを含まない行があるとき、その行のカードを消して、上へ詰める
数の書かれたカードを含まない列があるとき、その列のカードをのぞき、左へ詰める
座表圧縮とかいう奴と同じ結果になるのでは
"""
H, W, N = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N)]
A = list(map(lambda ab: ab[0], AB))
B = list(map(lambda ab: ab[1], AB))

a_temp = sorted(set(A))
ad = {v: i for i, v in enumerate(a_temp)}
ans_a = list(map(lambda v: ad[v] + 1, A))

b_temp = sorted(set(B))
bd = {v: i for i, v in enumerate(b_temp)}
ans_b = list(map(lambda v: bd[v] + 1, B))

for i in range(N):
    print(ans_a[i], ans_b[i])
