"""
UnionFindを使うことを考えられるが、UnionFindはつなげるのは得意だけど取り除くのは苦手
なので、手順を逆から考えていく
- まず全てのコストを合計する
- 次にコストの小さい順に変をソートする
- コストがマイナスの時
    - 外す意味がないのでつなげる
    - 繋げてコストの絶対値を合計にたす(一回マイナスを足しているので帳尻合わせ)
- コストがプラスの場合
    - 日連結ならつなげる
    - で合計コストからマイナスする
"""


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent_size = [-1]*n

    def leader(self, a):
        if self.parent_size[a] < 0:
            return a
        self.parent_size[a] = self.leader(self.parent_size[a])
        return self.parent_size[a]

    def merge(self, a, b):
        x, y = self.leader(a), self.leader(b)
        if x == y:
            return
        if abs(self.parent_size[x]) < abs(self.parent_size[y]):
            x, y = y, x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y] = x

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def size(self, a):
        return abs(self.parent_size[self.leader(a)])

    def groups(self):
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# ポイントを全て足し合わせる
point_sum = sum([e[2] for e in edges])
# コストの小さい順にソート数
sorted_edges = sorted(edges, key=lambda x: x[2])

un = UnionFind(N+1)
for a, b, cost in sorted_edges:
    if cost < 0:
        un.merge(a, b)
        point_sum += abs(cost)
        continue
    if un.same(a, b):
        continue
    # ポイントが小さいうちに繋げておく(後から出るものの方が外した時のポイントがでかい)
    un.merge(a, b)
    point_sum -= cost
print(point_sum)
