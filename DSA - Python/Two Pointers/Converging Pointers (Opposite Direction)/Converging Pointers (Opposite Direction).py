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


if __name__ == "__main__":
    nums = [1, 3, 4, 6, 8, 10]
    target = 14

    result = two_sum_sorted(nums, target)
    print(result)