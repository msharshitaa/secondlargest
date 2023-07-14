def find_second_largest(array):
    if len(array) < 2:
        return -1
    largest = max(array)
    second_largest = float('-inf')
    for num in array:
        if num != largest and num > second_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return -1
    else:
        return second_largest
array = list(map(int, input().split()))
result = find_second_largest(array)
print(result)
