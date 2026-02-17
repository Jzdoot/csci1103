numbers = [int(input()), int(input()), int(input())]

if numbers[0] <= numbers[1] and numbers[0] <= numbers[2]:
    print(numbers[0])
elif numbers[1] <= numbers[0] and numbers[1] <= numbers[2]:
    print(numbers[1])
else:
    print(numbers[2])
