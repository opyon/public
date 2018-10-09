def divisor_sum(n):
    result = [1]
    len_n = n // 2 + 1
    for i in range(2, len_n):
        if n % i == 0:
            result.append(i)
    return sum(result)


def amicable_numbers_sum(q):
    a = {}
    for i in range(1, q):
        a[i] = divisor_sum(i)

    total = 0
    for k, v in a.items():
        if k != v and (v, k) in a.items():
            total += k + v
    print(total // 2)


amicable_numbers_sum(10000)
# 31626
# https://projecteuler.net/problem=21
