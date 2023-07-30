# -*- coding: utf-8 -*-
"""
Q個のクエリに答える
クエリの内容
- L,R,Xが与えられる
- AL,...,ARのうち値がXに等しいものの数を答える
Aに含まれる数のうちインデックス番号でなん番目にあるかというリストを作る
"""
from bisect import bisect_left, bisect_right


N = int(input())
A = list(map(int, input().split()))
Q = int(input())
query_list = [list(map(int, input().split())) for _ in range(Q)]
index_list = [[] for _ in range(N+1)]
for i, a in enumerate(A):
    index_list[a].append(i+1)


class BinarySearch:
    def __init__(self, x_list, x):
        """
        argsに元になる配列とか条件の判定に使うものを入れるとよし
        何個でも可能
        """
        self.x_list = x_list
        self.x = x

    def is_ok_left(self, mid):
        """
        条件を満たすか考える
        今回の場合はx番目の要素が条件を満たすか
        """
        if self.x_list[mid] >= self.x:
            return True
        return False

    def is_ok_right(self, mid):
        if self.x_list[mid] > self.x:
            return True
        return False

    def bisect_left(self, ng, ok):
        '''
        初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
        まずis_okを定義すべし
        ng ok は  とり得る最小の値-1 とり得る最大の値+1
        最大最小が逆の場合はよしなにひっくり返す
        '''
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if self.is_ok_left(mid):
                ok = mid
            else:
                ng = mid
        return ok

    def bisect_right(self, ng, ok):
        '''
        bisect_right
        左側ではなく右側のindexを返す
        '''
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if self.is_ok_right(mid):
                ok = mid
            else:
                ng = mid
        return ok


for L, R, X in query_list:
    x_ind = index_list[X]
    if len(x_ind) == 0:
        print(0)
        continue
    lbn = BinarySearch(x_ind, L)
    rbn = BinarySearch(x_ind, R)
    l_ind = lbn.bisect_left(-1, len(x_ind))
    r_ind = rbn.bisect_right(-1, len(x_ind))
    print(r_ind-l_ind)


class BinarySearch:
    def __init__(self, args):
        """
        argsに元になる配列とか条件の判定に使うものを入れるとよし
        何個でも可能
        """
        self.args = args

    def is_ok_left(self, mid):
        """
        条件を満たす領域の最小値を求める
        besect_leftと同じ
        [1,3,5,7]で3の時にindexだと1を返す
        """
        pass

    def is_ok_right(self, mid):
        """
        条件を満たす領域の最大値を求める
        [1,3,5,7]で3の時にindexだと2を返す
        """
        pass

    def bisect_left(self, ng, ok):
        '''
        初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
        まずis_okを定義すべし
        ng ok は  とり得る最小の値-1 とり得る最大の値+1
        最大最小が逆の場合はよしなにひっくり返す
        '''
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if self.is_ok_left(mid):
                ok = mid
            else:
                ng = mid
        return ok

    def bisect_right(self, ng, ok):
        '''
        bisect_right
        左側ではなく右側のindexを返す
        '''
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if self.is_ok_right(mid):
                ok = mid
            else:
                ng = mid
        return ok
