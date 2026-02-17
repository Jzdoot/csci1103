decimal = int(input())

while decimal > 0:
    print(decimal % 2, end="")
    decimal = int(decimal / 2)
print()
