def understand_the_task():
    '''
    The Sieve of Eratosthenes is a simple and ingenious ancient algorithm for finding all prime numbers up to any given limit.
    A composite number is a positive integer that can be formed by multiplying two smaller positive integers, and is not prime.
    A prime number is a positive integer greater than 1 that cannot be formed by multiplying two smaller numbers (only ÷ 1 or itself).

    Steps:
    1. Generate a list of integers from 2 to ###
    2. Starting at 2, eliminate every second integer (all the multiples of 2)
    3. Starting at 3, eliminate every third integer (all the multiples of 3)
    4. Starting at 5, eliminate every fifth integer (all the multiples of 5)
    5. Starting at 7, eliminate every seventh integer (all the multiples of 7)
    6. Continue in this pattern until a prime number multiplied by itself is greater than the range
    7. The remaining integers will all be prime!
    '''
