L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

frequency = {}

for num in L1:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

most_frequent_num = None
max_count = 0

for num, count in frequency.items():
    if count > max_count:
        most_frequent_num = num
        max_count = count

print(f"Le nombre le plus frequent dans la liste est le : {most_frequent_num} ({max_count} fois)")

