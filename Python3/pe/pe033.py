result = []
for i in range(10, 100):
    for j in range(10, 100):
        if i <= j:
            continue

        i10 = i // 10
        i01 = i % 10
        j10 = j // 10
        j01 = j % 10

        if i01 == 0 or j01 == 0 or i10 == i01 or j10 == j01:
            continue

        d = j / i

        if (i10 == j10 and j01 / i01 == d) \
        or (i10 == j01 and j10 / i01 == d) \
        or (i01 == j10 and j01 / i10 == d) \
        or (i01 == j01 and j10 / i10 == d):
            result.append([i, j])

total = 1
for i, j in result:
    total *= i / j
print(int(total))
# 100
# https://projecteuler.net/problem=33
