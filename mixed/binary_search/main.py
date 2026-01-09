def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    attempt_counter = 0
    while left <= right:
        attempt_counter += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return f"Input: {target} | Index: {mid} | BigO: {attempt_counter}"
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = [1, 0, 3, 5, 9, 12]
arr.sort()
print(binary_search(arr, 9))

arr_2 = [-1, 0, 3, 5, 9, 12]
arr_2.sort()
print(binary_search(arr_2, 2))
