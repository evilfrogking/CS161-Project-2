"""
Primes.py
Carrie West
This program will prompt the user for a number and 
check for prime numbers up to that number.
"""

import math


prime_input = int(input ("This program will check for prime numbers.\
     Please enter a number between zero and one hundred. "))
print ("The number you entered is:", (prime_input))

def prime_number(num):
    if num < 2:
        return False
    for i in range (2, int(math.sqrt(num)) + 1): # take the input and use square root. 
         if num % i == 0: # if the answer is an integer than its not prime
              return False
    return True

print("The prime numbers in this range are: ")
prime_answer = [num for num in range(2, prime_input + 1) if prime_number(num)]
print(prime_answer)

z = input ("end, CWest")

