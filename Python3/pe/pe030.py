def digit_fifth_powers_sum(N):
    ans = 0
    for i in range(2, N):
        total = 0
        for j in str(i):
            total += int(j) ** 5
        if i == total:
            ans += total
    return ans


N = (9 ** 5) * 10
print(digit_fifth_powers_sum(N))
# 443839
# https://projecteuler.net/problem=30
