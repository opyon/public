def number_letter_counts(target):
    nums = {}
    nums[0] = ""
    nums[1] = "one"
    nums[2] = "two"
    nums[3] = "three"
    nums[4] = "four"
    nums[5] = "five"
    nums[6] = "six"
    nums[7] = "seven"
    nums[8] = "eight"
    nums[9] = "nine"
    nums[10] = "ten"
    nums[11] = "eleven"
    nums[12] = "twelve"
    nums[13] = "thirteen"
    nums[14] = "fourteen"
    nums[15] = "fifteen"
    nums[16] = "sixteen"
    nums[17] = "seventeen"
    nums[18] = "eighteen"
    nums[19] = "nineteen"
    nums[20] = "twenty"
    nums[30] = "thirty"
    nums[40] = "forty"
    nums[50] = "fifty"
    nums[60] = "sixty"
    nums[70] = "seventy"
    nums[80] = "eighty"
    nums[90] = "ninety"
    nums[100] = "hundred"
    nums[1000] = "thousand"

    ans = 0
    for i in range(1, target+1):
        if i < 1000:
            num100 = i
        else:
            ans += len(nums[i // 1000])
            ans += len(nums[1000])
            if i % 1000 == 0:
                continue
            else:
                ans += 3
            num100 = i % 1000

        if num100 >= 100:
            ans += len(nums[num100 // 100])
            ans += len(nums[100])
            if num100 % 100 == 0:
                continue
            else:
                ans += 3

        num10 = num100 % 100
        if num10 <= 20:
            ans += len(nums[num10])
        else:
            ans += len(nums[int(num10//10*10)])
            ans += len(nums[num10 % 10])
    return ans

print(number_letter_counts(1000))
# 21124
# https://projecteuler.net/problem=17