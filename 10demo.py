# 10demo.py by Xiaoran Yu

import math

print('Hello, again') # greeting

def gougu(a, b): return  math.sqrt(a**2 + b**2)

da_an = gougu(3, 4)
print(da_an)

#print(1 / 0)		# divide by zero error
#print(math.log(0))	# math domain error
#print(math.sqrt(-1))	# math domain error

a = 3				# side of triangle
b = 4				# side of triangle
c = math.sqrt(a**2 + b**2)	# hypotenuse
print(c)
