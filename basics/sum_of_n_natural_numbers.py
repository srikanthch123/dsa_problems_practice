# input = 10
# output = 55.0

#method1 
def sum_of_natural_numbers_1(number):
    """Calculate the sum of all natural numbers """
    return number * (number+1)//2

#method2
def sum_of_natural_numbers_2(number):
    """Calculate the sum of all natural numbers """
    sum=0
    for i in range(1,number+1):
        sum = sum+i 
    return sum

n=int(input())
print(sum_of_natural_numbers_1(n))
print(sum_of_natural_numbers_2(n))


# Let's analyze the time and space complexity of both functions:

# ### `sum_of_natural_numbers_1(number)`

# Time Complexity:
# - This function simply calculates the sum of natural numbers using the formula (n * (n + 1)) / 2.
# - Regardless of the value of 'number', the function only performs a few arithmetic operations.
# - Thus, the time complexity is constant, denoted as O(1).

# Space Complexity:
# - The function only uses a few variables to store the result and perform arithmetic operations.
# - The space complexity is also constant, denoted as O(1).

# ### `sum_of_natural_numbers_2(number)`

# Time Complexity:
# - This function uses a loop to iterate from 1 to 'number' and accumulates the sum.
# - The loop runs 'number' times.
# - Therefore, the time complexity is linear, denoted as O(n), where 'n' is the input number.

# Space Complexity:
# - The function uses a single variable 'sum' to accumulate the sum.
# - The space used is not dependent on the input size, so it remains constant.
# - The space complexity is O(1).

# ### Summary:

# - `sum_of_natural_numbers_1` has a time and space complexity of O(1).
# - `sum_of_natural_numbers_2` has a time complexity of O(n) and a space complexity of O(1).
