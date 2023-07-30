# -*- coding: utf-8 -*-
"""
解く前のメモ用
今回の問題だと答え未満だと条件を満たさない
答え以上だと条件を満たすというふうに、Xがでかいほど条件を満たしやすい
（Xが大きいほど売り手の数が当然増えやすいので）
"""
from bisect import bisect_right, bisect_left


class BinarySearch:
    def __init__(self, sellers, buyers):
        """
        sellers: 売り手のリスト(ソート済み)
        buyers: 買い手のリスト(ソート済み)
        """
        self.sellers = sorted(sellers)
        self.buyers = sorted(buyers)

    def sellers_cnt(self, x):
        """
        x円以上の売り手の数を返す
        """
        return bisect_right(self.sellers, x)

    def buyers_cnt(self, x):
        """
        x円以下の買い手の数を返す
        """
        ind = bisect_left(self.buyers, x)
        return len(self.buyers) - ind

    def is_ok(self, x):
        if self.sellers_cnt(x) >= self.buyers_cnt(x):
            return True

    def meguru_bisect(self, ng, ok):
        '''
        初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
        まずis_okを定義すべし
        ng ok は  とり得る最小の値-1 とり得る最大の値+1
        最大最小が逆の場合はよしなにひっくり返す
        '''
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if self.is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
bn = BinarySearch(A, B)
ans = bn.meguru_bisect(0, 10 ** 9 + 1)
print(ans)
