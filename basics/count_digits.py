# input = 2853
# output = 4 

def count_digits(n):
    count = 0
    while n != 0 :
        n = n // 10 
        count += 1 
    return count

number= int(input())
print(count_digits(number))


# Let's analyze the time and space complexity of the `count_digits` function:

# ### `count_digits(n)`

# Time Complexity:
# - The function iteratively divides the number by 10 until it becomes 0, counting the digits in the process.
# - The number of iterations depends on the number of digits in the input 'n'.
# - If 'n' has 'd' digits, the loop will iterate 'd' times.
# - Thus, the time complexity is linear with respect to the number of digits in 'n', denoted as O(d).

# Space Complexity:
# - The function uses a single variable 'count' to keep track of the number of digits.
# - Other variables are used for loop control which do not depend on the input size.
# - Therefore, the space complexity is constant, denoted as O(1).

# ### Summary:

# - The time complexity of `count_digits` is O(d), where 'd' is the number of digits in the input 'n'.
# - The space complexity of `count_digits` is O(1).

# These complexities represent the worst-case scenario where 'n' has the maximum number of digits.