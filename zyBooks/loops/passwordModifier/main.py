word = input()


str_from = ["i", "a", "m", "B", "s"]
str_to = ["1", "@", "M", "8", "$"]

for i in range(len(str_from)):
    password = ""
    for j in word:
        if j == str_from[i]:
            password += str_to[i]
        else:
            password += j
    # print(password)
    word = password
word += "!"
# print(f"final {word}")
print(word)
