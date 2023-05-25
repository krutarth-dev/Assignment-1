def twoSum(nums, target):
    num_map = {}  # dictionary to store the numbers and their indices
    
    for i, num in enumerate(nums):
        complement = target - num  # calculate the complement of the current number
        
        if complement in num_map:
            return [num_map[complement], i]  # return the indices if complement is found
            
        num_map[num] = i  # store the current number and its index in the dictionary
    
    return []  # return an empty list if no solution is found

nums = [7, 10, 21, 6]
target = 27
result = twoSum(nums, target)
print(result)
