"""
Nの方で全探索する
"""
N, K = map(int, input().split())
rest = K
cur = 0
visited = set()
ab = []
for i in range(N):
    a, b = map(int, input().split())
    ab.append((a, b))
ab = sorted(ab)
for i in range(N):
    a, b = ab[i]
    # 減らすべき数
    des = a - cur
    if a in visited:
        des = 0
    # a番目の村に到達できない場合
    if rest - des < 0:
        print(cur + rest)
        exit()
    rest += b
    rest -= des
    cur = a
    visited.add(a)
# さらにちょっと余った場合
print(cur + rest)
