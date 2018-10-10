import sys
import math
# 再帰回数の上限
# sys.setrecursionlimit(2100000000)
sys.setrecursionlimit(10000)

def fibo2(n_1, n_2, count):
    n = n_1 + n_2
    count += 1
    if n >= target:
        return count
    return fibo2(n, n_1, count)

# N = 1000で問題を解きたいのに
# N = 823以上になると結果が表示されない
# N = 823
N = 822
target = 10 ** (N-1)
print(fibo2(1, 1, 2))

# 検算
# N = 3
# 12