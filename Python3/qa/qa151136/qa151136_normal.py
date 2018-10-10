def fibo1(target):
    a, b = 1, 1
    cnt = 2
    target -= 1
    while b < 10 ** (target):
        cnt += 1
        a, b = b, a + b
    return cnt

target = 1000
print(fibo1(target))
# 出力結果
# 4782
# https://projecteuler.net/problem=25

# https://teratail.com/questions/151136