# -*- coding: utf-8 -*-
"""
英小文字と(と)からなる文字列Sが与えられる。Sの長さはNで与えられる。
以下の操作を可能な限り繰り返した後のSを出力する
- S の連続部分文字列であって、最初の文字が ( かつ 最後の文字が ) かつ 最初と最後以外に ( も ) も含まないものを自由に 
1 つ選び削除する
なお、操作を可能な限り繰り返したあとのSは操作の手順によらず一意に定まることが証明できます。
"""


def remove_parentheses(S):
    # 1. 最初に、文字列Sから条件を満たさない部分を削除する
    stack = []  # 開き括弧の位置を保存するスタック
    removes = []
    for i, c in enumerate(S):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if stack:
                start = stack.pop()
                # 開き括弧と閉じ括弧の間に、他の括弧が含まれていない場合に削除する
                has_parentheses = False
                for j in range(start + 1, i):
                    if S[j] == '(' or S[j] == ')':
                        has_parentheses = True
                        break
                if not has_parentheses:
                    removes.append((start, i))
    if removes:
        parts = []
        start = 0
        for i, j in removes:
            parts.append(S[start:i])
            start = j+1
        parts.append(S[start:])
        S = ''.join(parts)
    return S


N = int(input())
S = input()
while True:
    new_S = remove_parentheses(S)
    if new_S == S:
        break
    S = new_S
print(S)
