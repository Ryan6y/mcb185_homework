seq = 'GATTTCbbb'
s = 'ABCDEFGHIJ'
print(s[0:5:2])

nts = ['A', 'T', 'C']
print(nts)


nts.append('D')
print(nts)

first = nts.pop()
print(first)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)