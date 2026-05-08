def max_crossing(arr, left, mid, right):
    total = 0
    left_sum = float('-inf')
    max_left = mid

    for i in range(mid, left - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
            max_left = i

    total = 0
    right_sum = float('-inf')
    max_right = mid + 1

    for i in range(mid + 1, right + 1):
        total += arr[i]
        if total > right_sum:
            right_sum = total
            max_right = i

    return left_sum + right_sum, max_left, max_right


def max_subarray(arr, left, right):
    if left == right:
        return arr[left], left, right

    mid = (left + right) // 2

    left_res = max_subarray(arr, left, mid)
    right_res = max_subarray(arr, mid + 1, right)
    cross_res = max_crossing(arr, left, mid, right)

    return max(left_res, right_res, cross_res, key=lambda x: x[0])


# Example
arr = [-2,-3 ,4 ,-1 ,-2 ,1, 5,-3]

max_sum, start, end = max_subarray(arr, 0, len(arr) - 1)

print("Maximum Subarray:", arr[start:end+1])
print("Maximum Sum:", max_sum)