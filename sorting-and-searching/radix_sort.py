def get_max_digits(arr):
    max_num = max(arr)
    num_digits = 0
    while max_num > 0:
        num_digits += 1
        max_num //= 10
    return num_digits

def get_digit(num, position):
    # for i in range(position):
    #     num = num // 10
    # return num % 10
    return (num // (10 ** position)) % 10

def counting_sort_by_digit(arr, position):
    # Create buckets for digits 0-9
    buckets = [[] for _ in range(10)]

    # Put each number in the right bucket based on digit at position
    for num in arr:
        dig_at_position = get_digit(num, position)
        buckets[dig_at_position].append(num)
    
    # Flatten buckets back into arr
    return [num for digit_bucket in buckets for num in digit_bucket]

def radix_sort(arr):
    max_digit = get_max_digits(arr)

    for i in range(max_digit):
        arr = counting_sort_by_digit(arr, i)
    return arr

test = [170, 45, 75, 90, 2, 802, 24, 66]
print(f"Original: {test}")
sorted_arr = radix_sort(test.copy())
print(f"Sorted: {sorted_arr}")