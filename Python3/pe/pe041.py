import time
import math
import itertools as it


def get_primes(n):
    primes = [True] * n
    result = [2]
    for prime in range(3, n, 2):
        if primes[prime]:
            result.append(prime)
            for i in range(prime * prime, n, prime * 2):
                primes[i] = False
    return result


def is_prime(target, primes):
    for p in primes:
        if target % p == 0:
            return False
    return True


def get_pandigitals(n):
    d = [i for i in range(n , 0, -1)]
    return list(it.permutations(d))


def unpac_pd(num_itr):
    pd = 0
    for n in num_itr:
            pd = 10 * pd + n
    return pd


def lap():
    print(time.perf_counter() - time_start)


def main1(K):
    N = int(math.sqrt(10 ** K))
    primes = get_primes(N)
    for k in range(K, 6, -1):
        for num_itr in  get_pandigitals(k):
            pd = unpac_pd(num_itr)
            if is_prime(pd, primes):
                return pd


time_start = time.perf_counter()
K = 9
print(main1(K))
lap()
# 7652413
# 0.411590071
