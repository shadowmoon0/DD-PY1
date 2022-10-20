list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

m = list_numbers.index(max(list_numbers))
for i in range(len(list_numbers)):
    if list_numbers[i] == m:
        i = m
        break

list_numbers[-1], list_numbers[m] = list_numbers[m], list_numbers[-1]

print(list_numbers)