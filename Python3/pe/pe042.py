def get_word_score(word):
    offset = ord('A') - 1
    return sum([ord(c) - offset for c in word])

file_name_in = r'test\words.txt'
with open(file_name_in, "r", encoding = "utf-8") as open_file:
    src = open_file.read()
words = src.replace(r'"', '').split(",")

word_scores = [get_word_score(word) for word in words]
triangle_numbers = [(i * i + i) // 2 for i in range(1, max(word_scores) + 1)]
print(sum([1 for word_score in word_scores if word_score in triangle_numbers]))

# 162
# https://projecteuler.net/problem=42
