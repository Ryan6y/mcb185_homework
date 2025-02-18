def its_prime(n):
    for x in range(2, n, +1):
        if n % x == 0:
            return False
    return True

for i in range(51, 0, -2):
    if its_prime(i):
        print(f'{i}*')
    else:
        print(i)