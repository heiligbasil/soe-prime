

# Embed the docstrings in this function to be accessed by Help()
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


# Initialize the necessary variables
start_num: int = 2
ending_num: int = 120
looping_list: list = [2, 3, 5, 7, 9]
result_list: list = [True] * ending_num

# Cross off numbers in the list which are not prime via process of elimination
for i in looping_list:
    for j in range(i * 2, ending_num, i):
        result_list[j] = False

# Display the prime numbers to the console
print('Prime numbers: ', end='')
for i in range(start_num, ending_num):
    if result_list[i]:
        print(str(i), end=', ')

print('...')
