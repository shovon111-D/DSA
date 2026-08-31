def frequency_count(arr):
    # Find maximum value manually
    max_val = arr[0]

    for num in arr:
        if num > max_val:
            max_val = num

    # Create frequency array
    freq = [0] * (max_val + 1)

    # Count frequencies
    for num in arr:
        freq[num] += 1

    return freq


arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]

freq = frequency_count(arr)

# Print frequencies
for value in range(len(freq)):
    if freq[value] > 0:
        print(f"{value} appears {freq[value]} time(s)")