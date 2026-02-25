stringIn = input()

# Spliting the parts of the input
char = stringIn[0]
word = stringIn[2:]
count = word.count(char)
if count == 1:
    print(f"{count} {char}")
else:
    print(f"{count} {char}'s")
