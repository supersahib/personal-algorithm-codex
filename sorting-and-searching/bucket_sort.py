def get_bucket_index(value, num_buckets, min_val=0.0, max_val=1.0):
    # Step 1: Normalize to [0, 1)
    normalized_val = (value-min_val) / (max_val - min_val)
   
    # Step 2: Scale to bucket count
    index = int(normalized_val * num_buckets)
    
    return min(index, num_buckets - 1) 

def bucket_sort(arr, num_buckets=10):
    if len(arr) == 0:
        return arr
    # Find actual range
    min_val = min(arr)
    max_val = max(arr)
    if min_val == max_val:
      return 0

    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        num_idx = get_bucket_index(num, num_buckets, min_val, max_val)
        buckets[num_idx].append(num)

    for bucket in buckets:
        bucket.sort()

    return [num for bucket in buckets for num in bucket]

test1 = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
test2 = [3.2, 1.5, 4.8, 2.7, 3.9, 1.1, 4.2]  # Different range
test3 = [5, 2, 8, 1, 9, 3]  # Integers
test4 = [0.1, 0.11, 0.12, 0.13]  # Clustered values

for test in [test1, test2, test3, test4]:
    sorted_arr = bucket_sort(test.copy())
    print(f"Original: {test}")
    print(f"Sorted:   {sorted_arr}")
    print(f"Correct:  {sorted_arr == sorted(test)}\n")