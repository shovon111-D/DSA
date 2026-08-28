# Remove Duplicates from Sorted Array

> Removes duplicates **in-place** from a sorted array using the two-pointer technique, returning the count of unique elements.

## 📋 Overview

| Property | Value |
|---|---|
| **Time Complexity** | `O(n)` |
| **Space Complexity** | `O(1)` (in-place) |
| **Technique** | Two-pointer (slow/fast) |
| **Precondition** | Input array must be sorted |

## 🔧 Implementation

```python
def remove_duplicates(nums: list[int]) -> int:
    """Remove duplicates in-place from a sorted array and return new length."""
    if not nums:
        return 0

    slow = 0  # Points to the position of the last unique element

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1
```

## 💡 How It Works

1. `slow` tracks the last position of a confirmed unique element
2. `fast` scans ahead through the array
3. When `nums[fast]` differs from `nums[slow]`, it's a new unique value — advance `slow` and copy it in
4. Duplicates are simply skipped over; no extra array is allocated
5. Return `slow + 1` — the count of unique elements now sitting at the front

## ▶️ Example Usage

```python
if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 4, 4, 5]
    new_length = remove_duplicates(nums)
    print("New length:", new_length)
    print("Modified array:", nums[:new_length])
```

**Output:**

```
New length: 5
Modified array: [1, 2, 3, 4, 5]
```

## 🔍 Step-by-Step Trace

| `fast` | `nums[fast]` | `nums[slow]` | Action | Array State |
|---|---|---|---|---|
| 1 | 1 | 1 | skip (duplicate) | `[1,1,2,2,3,4,4,5]` |
| 2 | 2 | 1 | `slow→1`, copy | `[1,2,2,2,3,4,4,5]` |
| 3 | 2 | 2 | skip (duplicate) | `[1,2,2,2,3,4,4,5]` |
| 4 | 3 | 2 | `slow→2`, copy | `[1,2,3,2,3,4,4,5]` |
| 5 | 4 | 3 | `slow→3`, copy | `[1,2,3,4,3,4,4,5]` |
| 6 | 4 | 4 | skip (duplicate) | `[1,2,3,4,3,4,4,5]` |
| 7 | 5 | 4 | `slow→4`, copy | `[1,2,3,4,5,4,4,5]` |

Final: `slow = 4` → length `5` → `[1, 2, 3, 4, 5]`

## ⚖️ Edge Cases

| Input | Output | Notes |
|---|---|---|
| `[]` | `0` | Empty array handled early |
| `[1]` | `1` | Single element, no duplicates possible |
| `[1,1,1,1]` | `1` | All duplicates collapse to one |
| `[1,2,3]` | `3` | No duplicates, array unchanged |