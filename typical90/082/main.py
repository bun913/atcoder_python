# -*- coding: utf-8 -*-
"""
黒板に整数xをx回書く
黒板以下かれている文字の個数を数える(桁数)
3..5なら3を3回,4を4回,5を5回合計12桁の文字

L,Rが10**18なので、とてもforでは間に合わない
"""
L, R = list(map(int, input().split()))
mod = 10 ** 9 + 7


def count_number(number: int) -> int:
    digit, cnt = 1, 0
    while True:
        under = 10 ** (digit - 1) - 1
        top = min(number, 10 ** digit - 1)
        cnt += ((top * (top + 1) - under * (under+1)) // 2) * digit

        if number <= 10 ** digit - 1:
            return cnt
        digit += 1


print((count_number(R) - count_number(L-1)) % (10 ** 9 + 7))
