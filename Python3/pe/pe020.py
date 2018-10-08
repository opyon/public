import math


def factorial_digit_sum(n):
    return sum([int(s) for s in list(str(math.factorial(n)))])


print(factorial_digit_sum(100))

# 648
# https://projecteuler.net/problem=20