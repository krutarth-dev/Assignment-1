def merge(nums1, m, nums2, n):
    i = m - 1  # Pointer for the last element in nums1
    j = n - 1  # Pointer for the last element in nums2
    k = m + n - 1  # Pointer for the last position in the merged array
    
    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    # If there are any remaining elements in nums2, copy them to nums1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

nums1 = [7, 8, 9, 0, 0, 0]
m = 3
nums2 = [4, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  
