import sys

list=[]
for arg in sys.argv[1]:
    list.append(arg)

count = len(list)
for i in range(count):
    if (i+1) % 3 == 1:
    	rf = 1
    elif (i+1) % 3 == 2:
    	rf = 2
    elif (i+1) % 3 == 0:
    	rf = 3
    ls = list[i:(i+3)]
    codon = ''.join(ls)
    print(f"{i+1}\t{rf}\t{codon}")
    if i + 3 >= count:
        break

