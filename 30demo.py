import math

s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print(f"{len(s1)}")

print(s.upper())
print(s)

print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

print(f'{math.pi}')            # does nothing special
print(f'{math.pi:.3f}')        # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')    # exponent notation
print(f'{"hello world":>20}')  # right justify with space filler
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:<10} {10}')        # left justify

print('{} {:.3f}'.format('str.format', math.pi))
print('%s %.3f' % ('printf', math.pi))

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

#practice

abc = [1, 2, 3, 4, 5, 6]