def findErrorNums(nums):
    n = len(nums)
    num_set = set()
    duplicate = -1
    
    # Find the duplicate number
    for num in nums:
        if num in num_set:
            duplicate = num
            break
        else:
            num_set.add(num)
    
    # Find the missing number
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing = expected_sum - actual_sum + duplicate
    
    return [duplicate, missing]

nums = [1, 2, 2, 4]
result = findErrorNums(nums)
print(result) 
