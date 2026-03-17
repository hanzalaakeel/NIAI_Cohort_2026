#Square Root of a real or complex number with user & without user input

import cmath

num = 1 + 2j
# num = eval(input("Enter the number: "))
num_sqrt = cmath.sqrt(num)
print(f"The square root of {num} is {num_sqrt}")