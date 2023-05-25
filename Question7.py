def moveZeroes(nums):
    i = 0  # Pointer for the next position to store a non-zero element

    # Iterate through the array and find non-zero elements
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i] = nums[j]
            i += 1

    # Fill the remaining positions with zeros
    while i < len(nums):
        nums[i] = 0
        i += 1

nums = [0, 9, 0, 0, 15]
moveZeroes(nums)
print(nums)
