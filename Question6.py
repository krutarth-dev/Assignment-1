def containsDuplicate(nums):
    num_set = set()
    
    for num in nums:
        if num in num_set:
            return True
        else:
            num_set.add(num)
    
    return False

# Example usage
nums = [4, 2, 3, 4]
result = containsDuplicate(nums)
print(result)  # prints True
