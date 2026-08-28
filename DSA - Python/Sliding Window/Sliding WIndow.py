def Sliding_Window(arr, k):
    n = len(arr)
    if n < k:
        return []

    window_sum = sum(arr[:k])
    max_sum = window_sum
    result = [window_sum]

    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
        result.append(window_sum)

    return result, max_sum


if __name__ == "__main__":
    arr = [1, 3, 2, 5, 1, 1, 2]
    k = 3
    result, max_sum = Sliding_Window(arr, k)
    print(f"Sliding window sums: {result}")
    print(f"Maximum sum of any window of size {k}: {max_sum}")