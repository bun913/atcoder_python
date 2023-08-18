"""
制限を整理
1 <= L <= 10**9
1 <= Q <= 2*10**5
Unoin Findでクエリを逆から読んで繋げていくのもあり
(0,36)みたいに両端があって
(0,9,20)みたいにキルところを増やしていく
この時11を含む木材の長さは9,20がわかれば良いよねという考え
"""


class BinaryTree:
    def __init__(self, max_query=2*10**5, bitlen=30):
        n = max_query * bitlen
        self.nodes = [-1] * (2 * n)
        self.cnt = [0] * n
        self.id = 0
        self.bitlen = bitlen

    def size(self):
        return self.cnt[0]

    def count(self, x):
        pt = 0
        for i in range(self.bitlen-1, -1, -1):
            y = x >> i & 1
            if self.nodes[2*pt+y] == -1:
                return 0
            pt = self.nodes[2*pt+y]
        return self.cnt[pt]

    def insert(self, x):
        pt = 0
        for i in range(self.bitlen-1, -1, -1):
            y = x >> i & 1
            if self.nodes[2*pt+y] == -1:
                self.id += 1
                self.nodes[2*pt+y] = self.id
            self.cnt[pt] += 1
            pt = self.nodes[2*pt+y]
        self.cnt[pt] += 1

    def erase(self, x):
        if self.count(x) == 0:
            return
        pt = 0
        for i in range(self.bitlen-1, -1, -1):
            y = x >> i & 1
            self.cnt[pt] -= 1
            pt = self.nodes[2*pt+y]
        self.cnt[pt] -= 1

    def kth_elm(self, x):
        assert 1 <= x <= self.size()
        pt, ans = 0, 0
        for i in range(self.bitlen-1, -1, -1):
            ans <<= 1
            if self.nodes[2*pt] != -1 and self.cnt[self.nodes[2*pt]] > 0:
                if self.cnt[self.nodes[2*pt]] >= x:
                    pt = self.nodes[2*pt]
                else:
                    x -= self.cnt[self.nodes[2*pt]]
                    pt = self.nodes[2*pt+1]
                    ans += 1
            else:
                pt = self.nodes[2*pt+1]
                ans += 1
        return ans

    def lower_bound(self, x):
        pt, ans = 0, 1
        for i in range(self.bitlen-1, -1, -1):
            if pt == -1:
                break
            if x >> i & 1 and self.nodes[2*pt] != -1:
                ans += self.cnt[self.nodes[2*pt]]
            pt = self.nodes[2*pt+(x >> i & 1)]
        return ans


bt = BinaryTree()
L, Q = map(int, input().split())
# 両端を追加
bt.insert(0)
bt.insert(L)
for _ in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        bt.insert(x)
        continue
    # 二分探索でx以上の最小要素を探す
    p = bt.lower_bound(x)
    print(bt.kth_elm(p) - bt.kth_elm(p-1))
