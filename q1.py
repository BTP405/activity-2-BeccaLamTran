def getPrimeNumbers(n):
	""" Returns a list of prime numbers up to n. """
	prime_numbers = [] # Initialize an empty list to store prime numbers
	for i in range (2, n + 1): # Iterate through numbers 2 to n, inclusive
		if isPrime(i): # call isPrime function to check if the number is prime
			prime_numbers.append(i) # If prime, add to list
	return prime_numbers # Return the list of prime numbers

def isPrime(n):
	""" Check if n is a prime number.
 Parameters:
	n (int): The number to be tested
 
 Returns:
	bool: True if n is prime, False otherwise 
 	"""
	if n == 1: # 1 is not considered a prime number, so return False
		return False
	for i in range(2, int(n**0.5) + 1): # Iterate through numbers 2 to square root of n
		if n % i == 0: # If n is divisible by any number other than 1 and itself
			return False # Then the number is not prime, return False
	return True # No divisors found, then it is prime so return True