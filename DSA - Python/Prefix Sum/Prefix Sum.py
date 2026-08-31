def prefix_sum_with_zero(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix

if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9]
    prefix = prefix_sum_with_zero(arr)
    print(prefix)  # [0, 3, 4, 8, 9, 14, 23]

    # Sum of arr[l:r+1]
    l, r = 1, 3
    print(prefix[r + 1] - prefix[l])  # 1 + 4 + 1 = 6