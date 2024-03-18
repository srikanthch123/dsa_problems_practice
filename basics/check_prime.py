# input = 2
# output = True
 


def is_prime_1(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def is_prime_2(n):
    if n == 1:
        return False
    factors=0
    for i in range(1,n+1):
        if n % i == 0:
            factors += 1
    if factors == 2:
        return True
    else:
        return False

n= int(input())
print(is_prime_2(n))
print(is_prime_1(n))


# Both methods, `is_prime_1` and `is_prime_2`, are used to check whether a given number `n` is prime or not. Let's analyze the time and space complexity of each method:

# ### `is_prime_1`:

# - Time Complexity: O(n)
#   - The function iterates through all numbers from 2 to n - 1 to check if n is divisible by any of them. Therefore, the time complexity is linear in terms of n.

# - Space Complexity: O(1)
#   - The function uses only a constant amount of additional space, regardless of the input size n.

# ### `is_prime_2`:

# - Time Complexity: O(n)
#   - Similar to `is_prime_1`, the function iterates through all numbers from 1 to n to count the factors of n. Therefore, the time complexity is also linear in terms of n.

# - Space Complexity: O(1)
#   - The function uses only a constant amount of additional space, regardless of the input size n.

# Both functions have the same time complexity, but `is_prime_2` has an additional overhead of counting factors, which makes it slightly less efficient compared to `is_prime_1`. However, both methods have room for improvement as you only need to check up to the square root of n to determine if it's prime, rather than checking all numbers up to n. This would significantly reduce the time complexity for large inputs.