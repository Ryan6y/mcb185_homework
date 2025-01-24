# 10demo.py by Xiaoran Yu

import math

print('hello, again') # greeting

s = 'hello world'
print(s, type(s))

a = 0.3
b = 0.1 * 3
print (a, b)
if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')

print(abs(a - b)) # 5.551115123125783e-17
if abs(a - b) < 1e-9: print('close enough')

def circle_area(r): return math.pi * r**2
def rectangle_area(w, h): return w * h
def triangle_area(w, h): return rectangle_area(w, h) / 2
r=2
w=3
h=4
print (circle_area(r))
print (rectangle_area(w, h))
print (triangle_area(w, h))


