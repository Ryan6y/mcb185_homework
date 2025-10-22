##Unit1 assesment by Xiaoran Yu and Reese Carlsom

#first question
import math

def dis(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(dis(0, 0, 3, 4))
print(dis(0, 0, 2, 2))

#second question
def vp(a):
    if a <= 1 and a >= 0:
    	return 'valid'
    else: 
    	return 'invalid'

print(vp(9))
print(vp(0.345))
print(vp(-0.1))

#Third question
def pos2rf(a):
    if a % 3 == 1:
    	return 'Reading Frame 1'
    if a % 3 == 2:
    	return 'Reading Frame 2'
    if a % 3 == 0
    	return 'Reading Frame 3'

print(pos2rf(1))
print(pos2rf(1000))
print(pos2rf(9))

#Forth Question
def maxin4(a, b, c, d):
	if a > b > c > d: return a
	if b > c > d: return b
	if c > d: return c
	else: return d

print(maxin4(1, 2, 3, 4))
print(maxin4(3, 4, 100, 22))
print(maxin4(10000, 2, 345, 777))
