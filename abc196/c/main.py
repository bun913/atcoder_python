"""
解く前のメモ

普通にやるなら1から順に数えるけど数が大きすぎるので無理

と思ったけど半分に分けたら10**6なので間に合うという
"""
N = input()

for i in range(1, 1000001):
    s = str(i) + str(i)
    if int(s) > int(N):
        print(i-1)
        exit()
