from collections import deque

N = int(input())
A = list(map(int, input().split()))

q = deque([])
is_reverse = False

for a in A:
    if is_reverse:
        q.appendleft(a)
    else:
        q.append(a)
    is_reverse = not is_reverse

b = list(q)
if is_reverse == True:
    b.reverse()
print(*b)
