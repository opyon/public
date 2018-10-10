# @LouiS0616さん回答より追記
from functools import lru_cache

# 再帰回数の上限
import sys
# sys.setrecursionlimit(2100000000)
sys.setrecursionlimit(10000)

# @LouiS0616さん回答より追記
# @lru_cache(maxsize=None)
@lru_cache(maxsize=8)
def fibo(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    return fibo(n-1) + fibo(n-2)

# 元のコードのままだと@lru_cache(maxsize=8)を追記しても効果が無かった。
# @LouiS0616さん回答のように関数を分割すると動いた。
def main(target):
    i = 0
    while(True):
        if fibo(i) >= target:
            return i
        i += 1

N = 1000
target = 10 ** (N - 1)
print(main(target))
#4782
# https://projecteuler.net/problem=25

# https://teratail.com/questions/151136