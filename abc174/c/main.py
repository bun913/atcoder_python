"""
数列はどんどん10倍+7になっていく
数列をKで割ってあまりが0になるまで繰り返すわけだが
あまりはどこかで必ず循環する
あまりのパターンはK-1通りが最大なのでそこまで繰り返せばOK
"""
K = int(input())

cur = 7 % K
for i in range(K):
    if cur % K == 0:
        print(i+1)
        exit()
    cur *= 10
    cur += 7
    cur %= K
print(-1)
