def find_min_max(arr):

    if not arr:
        return None

    min_val = arr[0]
    max_val = arr[0]

    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return (min_val, max_val)

arr1 = [3, 2, 1, 56, 10000, 167]
result1 = find_min_max(arr1)
print(result1)

arr2 = [1, 345, 234, 21, 56789]
result2 = find_min_max(arr2)
print(result2)

arr3 = [56789]
result3 = find_min_max(arr3)
print(result3)