def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    """Merge two sorted arrays into one sorted array."""
    p1, p2 = 0, 0
    merged = []

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] <= arr2[p2]:
            merged.append(arr1[p1])
            p1 += 1
        else:
            merged.append(arr2[p2])
            p2 += 1

    # Append remaining elements
    merged.extend(arr1[p1:])
    merged.extend(arr2[p2:])

    return merged