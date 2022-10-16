import time
import math

print('Using the Math module I will find factorials, raise numbers to a power, and find the greatest common divisor.')
print('Enter the number you want to find the factorial of')
factor = int(input())
print(math.factorial(factor))
print('Enter the base number')
base = int(input())
print('Enter the exponent')
exp = int(input())
print(math.pow(base,exp))
print('Enter the first number to find the GCD')
one = int(input())
print('Enter the second number to find the GCD')
two = int(input())
print(math.gcd(one,two))
time.sleep(5)