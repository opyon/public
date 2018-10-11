from numba import jit


@jit(nopython = True)
def eratosthenes_boo(n):
    n += 1
    sieve = [True] * n
    sieve[0] = sieve[1] = False

    for i in range(4, n, 2):
        sieve[i] = False

    for prime in range(3, n, 2):
        if sieve[prime]:
            for i in range(prime * prime, n, prime * 2):
                sieve[i] = False
    return sieve


@jit(nopython = True)
def main1(primes):
    result = [0, 0]
    # 全探索
    # |a|<1000,|b|<=1000
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            while(True):
                chk = (n ** 2 + a * n + b)
                if chk > 1 and primes[chk] == True:
                    n += 1
                else:
                    # n=非素数で終了
                    ret = n + 1
                    break

            # 終了時にn最大値とa*bを更新
            if result[0] < n:
                ab = a * b
                result = [n, ab ]

    return result[1]


# 処理概要
# 素数リスト生成
# ループで数式の結果を素数判定しnをカウント
# n最大値とa*bを更新
# 結果出力
print(main1(eratosthenes_boo(100000)))
# -59231
# https://projecteuler.net/problem=27
