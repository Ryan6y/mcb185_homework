for i in range(51, 0, -2):
    is_prime = True  
    for den in range(2, i // 2 + 1):
        if i % den == 0:
            is_prime = False 
    
    if is_prime and i > 1:  
        print(f"{i}*")
    else:
        print(i)