def find_max(list1):
    max_number = list1[0]
    for i in list1:
        if i <= max_number:
            max_number = i
    return max_number

print(find_max([1,2,3,4,5]))