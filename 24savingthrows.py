import random

i = random.randint(1, 21)

def dc(n):
    if n >= i:
        return('saved')
    else:
        return('died')

print (dc(5))
print (dc(10))
print (dc(15))