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


if __name__ == "__main__":
    
    nums = [1, 1, 2, 2, 3, 4, 4, 5]
    new_length = remove_duplicates(nums)
    print("New length:", new_length)
    print("Modified array:", nums[:new_length])