def main1(n):
    if n == 1:
        return 1
    elif n < 1:
        return None

    n = n // 2 + 1

    total = 0
    for i in range(1, n):

#表計算で規則性を探す
#https://gyazo.com/6d3bfe3acc6efb2c231af2e23ac8f486

#         #愚直に式を書いてみる
#         a_1 = ((i - 1) * 2 + 1) ** 2
#         a = (i * 2 + 1)
#         b = a ** 2
#         c = b - a_1
#         d = c // 4
#         e = 4 * b - d * 6
#         total += e
#         print(i, a_1, a, b, c, d, e, total)

#        #全て代入すると変数がiのみになる
#         total += 4 * ( (i * 2 + 1)**2 ) - ((i * 2 + 1) ** 2 - ((i - 1) * 2 + 1) ** 2) // 4 * 6

        # 方程式を簡素化
        total += 16 * (i ** 2) + 4 * i + 4
    return total + 1


n = 1001
print(main1(n))
# 669171001
# https://projecteuler.net/problem=28