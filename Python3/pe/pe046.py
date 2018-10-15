def get_primes_boo(n):
    n += 1
    result = [1] * n
    result[0] = 0
    result[1] = 0

    for i in range(4, n, 2):
        result[i] = 0

    for prime in range(3, n, 2):
        if result[prime]:
            for i in range(prime * prime, n, prime * 2):
                result[i] = 0
    return result


def main1():
    primes = get_primes_boo(10000)
    start = 5
    step = 2
    for i, b in enumerate(primes[start::step]):
        if b == 0:
            j = 1
            while(True):
                ans_chk = 1
                chk = (start + i * step) - (j ** 2) * 2
                if chk < 2: break

                if chk > 1 and primes[chk] :
                    ans_chk = 0
                    break
                j += 1

            if ans_chk:
                return start + i * step


def lap():
    print('{:0.5f}/s'.format(time.perf_counter() - time_start))


import time
time_start = time.perf_counter()
print(main1())
lap()
# 5777
# 0.00521/s
# https://projecteuler.net/problem=46