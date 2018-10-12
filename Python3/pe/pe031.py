# def coin_sums(remainder, coin):
#     global total
#     if coin < 0:
#         total += 1
#         return
#     n = remainder // coins[coin]
#     for i in range(n + 1):
#         coin_sums(remainder - i * coins[coin], coin - 1)
#
# coins = [2, 5, 10, 20,50, 100, 200]
# total = 0
# coin_sums(200, len(coins)-1)
# print(total)
# 73682

# https://teratail.com/questions/151616
# @hayataka2049さんの回答を参考に、
# globalを使わないよう修正
def coin_sums2(remainder, coin):
    if coin < 0:
        return 1
    n = remainder // coins[coin]
    total2 = 0
    for i in range(n + 1):
        total2 += coin_sums2(remainder - i * coins[coin], coin - 1)
    return total2


coins = [2, 5, 10, 20, 50, 100, 200]
ans = coin_sums2(200, len(coins) - 1)
print(ans)
# 73682
# https://projecteuler.net/problem=31

