i = 51

while i >= 3:
    i = i - 2
    if i % 2 == 0:
        print(i)
    elif i % 3 == 0:
        print(i)
    elif i % 5 == 0:
        print(i)
    else:
        print(f"{i}*")
    
