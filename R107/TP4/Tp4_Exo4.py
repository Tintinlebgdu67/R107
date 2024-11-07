L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

most_frequent_num = None
max_count = 0
for num in L1:

    count = L1.count(num)
    if count > max_count:
        most_frequent_num = num
        max_count = count

print(f"Le nombre le plus frequent dans la liste est le : {most_frequent_num} ({max_count} fois)")


