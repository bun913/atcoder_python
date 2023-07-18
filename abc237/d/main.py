from collections import deque

N = int(input())
q = deque([N])
S = list(input())
# 逆順に処理していけば良い
for i in range(N-1, -1, -1):
    s = S[i]
    if s == 'R':
        q.appendleft(i)
        continue
    q.append(i)
print(*q)
