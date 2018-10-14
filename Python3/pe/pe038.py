def pandigital_multiples():
    chk = '123456789'
    max_num = 987654321
    i = 0
    result = 0
    while(True):
        if i > 10000:
            break
        i += 1
        s = ''
        for j in range(1, 10):
            n = i * j
            s += str(n)
            q = int(s)
            if max_num < q:
                break
            if len(s) == 9:
                if chk == (''.join(sorted(s))):
                    if result < q:
#                         print(q, i, j, n)
                        result = q
    return result
print(pandigital_multiples())
# 932718654
# https://projecteuler.net/problem=38

# 123456789 9 1 9
# 918273645 45 9 5
# 926718534 18534 9267 2
# 927318546 18546 9273 2
# 932718654 18654 9327 2
