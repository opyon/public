import timeit
import math

'''
#最終清書
'''

# 新：エラトステネスの篩：最終
def eratosthenes_sieve(n):
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

# 新：区間篩：最終
def primesList(n):
        n -= 1
        SIEVE_MAX = int(math.sqrt(n)) + 1
        primes = []
        sieve = eratosthenes_sieve(SIEVE_MAX - 1)

        for i in range(len(sieve)):
            if sieve[i]:
                primes.append(i)

        for i in range(1, (n // SIEVE_MAX) + 1):

            sieve = [True] * len(sieve)
            start_index = SIEVE_MAX * i

            for p in primes:
                if (p * p > start_index + SIEVE_MAX):
                    break

                jj = (p - (start_index % p)) % p

                for j in range(jj, SIEVE_MAX, p):
                    sieve[j] = False
#                     print('jj:',jj,'start:',start_index,'end:',start_index + SIEVE_MAX,'p:', p,'j:',start_index +j)

            for j in range(min([n - start_index + 1, SIEVE_MAX])):
                if sieve[j]:
                    primes.append(start_index+j)

        return primes


# 旧：エラトステネスの篩：比較用
def eratosthenes_list(n):
    primes = [True] * n
    result = [2]
    for prime in range(3, n, 2):
        if primes[prime]:
            result.append(prime)
            for i in range(prime * prime, n, prime * 2):
                primes[i] = False
    return result


def test(nn,test_on):
    if test_on:
        for nn in range(10, nn, nn // 10):
            a = eratosthenes_list(nn)
            b = primesList(nn)
            if not a == b:
                print('nn:', nn)
                print("miss")
                print(len(a), len(b))
                print(a)
                print(b)
                break
        else:
            print("all ok")

#     修正後テスト
#     print('区間篩修正:',timeit.timeit(lambda: (primesList(nn)), number = 1))
#     print('旧篩　　　:',timeit.timeit(lambda: (eratosthenes_list(nn)), number = 1))

#     print('区間篩修正:',timeit.timeit(lambda: print((primesList(nn))), number = 1))
#     print('旧篩　　　:',timeit.timeit(lambda: print((eratosthenes_list(nn))), number = 1))

#     print('区間篩修正:',timeit.timeit(lambda: print(len(primesList(nn))), number = 1))
#     print('旧篩　　　:',timeit.timeit(lambda: print(len(eratosthenes_list(nn))), number = 1))


nn = 10 ** 3
# 区間篩修正: 0.0002253680000000001
test(nn,0)

'''
#以下過去ログ
'''
# 新：区間篩：修正１
# nn = 100000000
# 区間篩修正: 17.563386085

# 新：区間篩：質問時初期
# nn = 100000000
# 24.349327380000002

# 旧：エラトステネスの篩：比較用
# nn = 100000000
# 11.725847288999997

# test確認用

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#                10 4個
#              100 25個
#           1,000 168個
#           2,000 303個
#         10,000 1,229個
#       100,000 9,592個
#    1,000,000 78,498個
#  10,000,000 664,579個
# 100,000,000 5,761,455個
