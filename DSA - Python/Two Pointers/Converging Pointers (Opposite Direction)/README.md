# Two Sum (Sorted Array)

Find two numbers in a **sorted** array that sum to a target value, using the two-pointer technique.

## Code

```python
def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    """Find two numbers in a sorted array that sum to target."""
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need a larger sum
        else:
            right -= 1  # Need a smaller sum
    return []
```

## How It Works

Two pointers start at opposite ends of the array and move toward each other:

| Step | Condition | Action |
|------|-----------|--------|
| 1 | `current_sum == target` | Match found — return indices |
| 2 | `current_sum < target` | Move `left` pointer right (increase sum) |
| 3 | `current_sum > target` | Move `right` pointer left (decrease sum) |

The array being **sorted** is what makes this work: moving `left` forward can only increase the sum, and moving `right` backward can only decrease it, so the pointers converge on the answer without backtracking.

## Complexity

| Metric | Value | Why |
|--------|-------|-----|
| Time | `O(n)` | Each pointer moves at most `n` times total |
| Space | `O(1)` | Only two index variables used |

## Example

```python
nums = [2, 7, 11, 15]
target = 9

two_sum_sorted(nums, target)  # -> [0, 1]  (2 + 7 == 9)
```

**Trace:**

| left | right | nums[left] | nums[right] | sum | vs target |
|------|-------|-----------|-------------|-----|-----------|
| 0 | 3 | 2 | 15 | 17 | too high → `right -= 1` |
| 0 | 2 | 2 | 11 | 13 | too high → `right -= 1` |
| 0 | 1 | 2 | 7  | 9  | **match** → return `[0, 1]` |

## Notes

- Returns an **empty list** if no pair sums to `target`.
- Assumes `nums` is sorted in ascending order — unsorted input gives incorrect results without warning.
- For unsorted input, a hash-map approach (`O(n)` time, `O(n)` space) is the standard alternative.