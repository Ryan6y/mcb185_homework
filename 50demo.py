s = {'A','C',"G"}
s.add('T')
print(s)
d = dict()
d = {'dog': 'woof', 'cat': 'meow'}
print(d['dog'])

for key in d: 
	print(f'{key} says {d[key]}')

for thing in d.items(): 
	print(thing[0], thing[1])