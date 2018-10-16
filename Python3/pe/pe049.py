def get_primes_list(n):
    sieve = [1] * n
    result = [2]
    for prime in range(3, n, 2):
        if sieve[prime]:
            result.append(prime)
            for i in range(prime * prime, n, prime * 2):
                sieve[i] = 0
    return result


def main1():
    primes = get_primes_list(10000)
    i = 1488
    offset = 3330
    while(i < 3340):
        n = [0, 0, 0]
        ans = 1
        for j in range(3):
            n[j] = offset * j + i
            if not n[j] in primes or sorted(str(n[j])) != sorted(str(n[0])):
                ans = 0
                break
        if ans:
            return int(''.join([str(x) for x in n]))
        i += 1


def lap():
    print('{:0.5f}/s'.format(time.perf_counter() - time_start))


import time
time_start = time.perf_counter()
print(main1())
lap()
# 296962999629
# 0.02158/s
# https://projecteuler.net/problem=49