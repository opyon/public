def collatz(n, count):
    if n in collatzs:
        return count + collatzs[n]

    if n == 1:
        return count + 1

    if n % 2  == 1:
        n = n * 3 + 1
    else:
        n = n //2

    count += 1
    return collatz(n, count)

def main(target):
    for i in range(1,target+1):
        collatzs[i] = collatz(i,0)

collatzs = {}
main(1000000)
print(max(collatzs, key=collatzs.get))
print(max(collatzs.items(),key=lambda x: x[1]))
# 837799
# (837799, 525)

# https://projecteuler.net/problem=14
# 正の整数に以下の式で繰り返し生成する数列を定義する.
# n → n/2 (n が偶数)
# n → 3n + 1 (n が奇数)
#
# 13からはじめるとこの数列は以下のようになる.
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
