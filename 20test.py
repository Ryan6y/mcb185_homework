#first question
import math

def dis(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(dis(1, 2, 3, 4))

#second question
def vp(a):
    if a <= 1 and a >= 0:
    	return 'valid'
    else: return 'not valid'

print(vp(9))
print(vp(0.345))
print(vp(-0.1))

#third question

