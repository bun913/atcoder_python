"""
Atcoderの問題解く用

1行1列データ

#str型で受け取るとき
s = input() 
#int型で受け取るとき
s = int(input()) 
#float型　(小数)で受け取るとき
s = float(input())

(1,N)行列データ
s = input().split()
# listで整数で受け取る
l = list(map(int, input().split()))

その他
https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785
"""
# 1..nまでの整数でmで割り切れるものの数は n/m個
# mが何回登場するかって考えでしょ、じゃあn//mじゃん

a, b, x = list(map(int, input().split()))

def count_of_div(n, m):
    return n // m

# 1以上b以下までの個数から
# 1以上a-1以下までの個数
# を引けば良い
a_count = count_of_div(a-1,x)
b_count = count_of_div(b,x)
print(b_count-a_count)
