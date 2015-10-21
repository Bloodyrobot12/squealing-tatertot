# Inport functions
import math
import time
import sys

# Show range and wait for 1 second
print ('Printing all prime numbers between 1 and 100')
time.sleep(1)

# Set function isPrime to check if a number is prime
def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0: 
            return False;
    return n>1;

# Print the numbers in the range if they are prime
for n in range(0, 100):
    if isPrime(n):
        print (n)

input('Press enter to exit...')
sys.exit()
