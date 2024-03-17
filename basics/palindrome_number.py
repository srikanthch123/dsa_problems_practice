# input = 5445
# output = True

def is_palindrome(n):
    rev = 0
    temp = n 
    while temp != 0 :
        digit = temp % 10
        rev = rev *  10 + digit
        temp = temp // 10
    return True if rev == n else False

number = int(input())
print(is_palindrome(number))

# Let's analyze the time and space complexity of the `is_palindrome` function:

# ### `is_palindrome(n)`

# Time Complexity:
# - The function iteratively reverses the input number 'n' and compares it with the original number to check if it's a palindrome.
# - The time complexity primarily depends on the number of digits in the input number 'n'.
# - Reversing the number involves iterating through each digit, which takes O(d) time, where 'd' is the number of digits in 'n'.
# - The comparison operation takes constant time.
# - Therefore, the overall time complexity is linear with respect to the number of digits in 'n', denoted as O(d).

# Space Complexity:
# - The function uses a few variables such as 'rev', 'temp', and 'digit' to perform operations.
# - The space used by these variables is not dependent on the input size and remains constant regardless of the value of 'n'.
# - Therefore, the space complexity is O(1).

# ### Summary:

# - The time complexity of `is_palindrome` is O(d), where 'd' is the number of digits in the input 'n'.
# - The space complexity of `is_palindrome` is O(1).

# These complexities represent the worst-case scenario where 'n' has the maximum number of digits.