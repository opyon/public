from numba import jit


@jit(nopython = True)
def get_primes_list(n):
    sieve = [1] * n
    result = [2]
    for prime in range(3, n, 2):
        if sieve[prime]:
            result.append(prime)
            for i in range(prime * prime, n, prime * 2):
                sieve[i] = 0
    return result


@jit(nopython = True)
def prime_factorization(x, primes):
    result = set()
    while(True):
        for prime in primes:
            if x % prime == 0:
                x //= prime
                result.add(prime)
                if x == 1:
                    return len(result)
            else:
                continue


@jit(nopython = True)
def main1(N):
#     素数リスト
    primes = get_primes_list(150000)

    i = 2
    while(True):
        # 連続した数の中に素数があるかチェック
        tmp = 0
        for j in range(i, i + N):
            if j in primes:
                tmp = j

        # 最後に見つかった素数の次までスキップ
        if tmp > 0:
            i = tmp + 1
            continue

        # 連続した数の中に素数がない状態
        ans = 1
        for j in range(N):
            # 素因数の個数判定
            if (prime_factorization(i + j, primes)) != N:
                i += (j + 1)
                ans = 0
                break

        # 全てのチェックを通れば答え
        if ans:
            return i


def lap():
    print('{:0.5f}/s'.format(time.perf_counter() - time_start))


import time
time_start = time.perf_counter()
print(main1(4))
lap()
# 134043
# 6.49709/s

# 総当たりなので遅い
# 全てに@jitを使っても６秒以上掛かる
# https://projecteuler.net/problem=47
