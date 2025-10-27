#20demo by Xiaoran

import sys

n = int(sys.argv[1])

def facto(n):
    for den in range(2, n // 2 + 1):
        if n % den == 0: return False
    return True

print(facto(n))