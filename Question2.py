def removeElement(nums, val):
    k = 0  # pointer for the next available position to store elements not equal to val
    
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]  # store the element not equal to val at position k
            k += 1  # move the pointer to the next available position
    
    return k

nums = [4, 3, 9, 3]
val = 3
k = removeElement(nums, val)
print(k)  
print(nums[:k]) 
