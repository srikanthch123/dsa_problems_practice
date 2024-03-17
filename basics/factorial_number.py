# input = 4
# output = 24 

def factorial_number(n):
    res = 1
    for i in range(2,n+1):
        res = res * i 
    return res

number = int(input())
print(factorial_number(number))



# Let's analyze the time and space complexity of the `factorial_number` function:

# ### `factorial_number(n)`

# Time Complexity:
# - The function calculates the factorial of the input number 'n' using a loop that iterates from 2 to 'n'.
# - In each iteration, a multiplication operation is performed.
# - The loop runs 'n' times.
# - Therefore, the time complexity is linear with respect to the input number 'n', denoted as O(n).

# Space Complexity:
# - The function uses a single variable 'res' to store the factorial result.
# - Other variables like 'i' and loop control variables require constant space.
# - Therefore, the space complexity is constant, denoted as O(1).

# ### Summary:

# - The time complexity of `factorial_number` is O(n), where 'n' is the input number.
# - The space complexity of `factorial_number` is O(1).

# These complexities represent the worst-case scenario where 'n' is the input number.