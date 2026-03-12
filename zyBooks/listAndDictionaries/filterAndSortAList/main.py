arry = [int(i) for i in input().split()]
negSort = []

for i in arry:
    if i < 0:
        negSort.append(i)
negSort.sort(reverse=True)
for i in negSort:
    print(i, end=" ")
