def plusOne(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):  # Start from the last digit and move towards the first digit
        if digits[i] != 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    
    # If all digits were 9, we need to add an additional digit 1 at the beginning
    return [1] + digits

digits = [1, 2, 7]
result = plusOne(digits)
print(result)  # prints [1, 2, 8]
