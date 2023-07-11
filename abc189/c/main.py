"""
lとrは全探索してもギリギリ間に合う
てことはlからrの距離は絶対にどんどん離れていく（全てとおる）
ので最小のaは随時更新していけば良いということ
"""
N = int(input())
A = list(map(int, input().split()))

ans = -1
for l in range(N):
    mini_a = A[l]
    for r in range(l, N):
        mini_a = min(mini_a, A[r])
        ans = max(ans, mini_a * (r - l + 1))
print(ans)
