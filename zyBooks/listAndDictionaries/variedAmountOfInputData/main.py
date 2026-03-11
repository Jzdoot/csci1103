from statistics import mean
number_arry =  [ float(i) for i in input().split() ]

print(f"{max(number_arry):.2f} {mean(number_arry):.2f}")
