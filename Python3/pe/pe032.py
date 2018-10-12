def main1():
    correct = list('123456789')
    total_set = set()
    for i in range(2000):
        for j in range(1000):
            ij = i * j
            chk = sorted(str(i) + str(j) + str(ij))
            if chk == correct:
                total_set.add(ij)
    return sum(total_set)
print(main1())
# 45228
# https://projecteuler.net/problem=32

# test
correct_test = list('123')
chk_test = sorted('3' + '1' + '2')
print(chk_test == correct_test)

