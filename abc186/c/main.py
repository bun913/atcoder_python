# -*- coding: utf-8 -*-
"""
次は10進数を8進数に変換するメソッドを自作した場合
"""
N = int(input())
ans = 0


def get_oct(x: int) -> str:
    n = x
    s = ''
    while n > 0:
        first = n % 8
        s = str(first) + s
        n //= 8
    return s


def judge(s: str) -> bool:
    if s.find("7") == -1:
        return True


ans = 0
for i in range(1, N+1):
    oc = get_oct(i)
    str_num = str(i)
    if judge(oc) is True and judge(str_num) is True:
        ans += 1
print(ans)
