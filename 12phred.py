# 12ohred.py by Xiaoran Yu

import math

def char_to_prob(char):
    
    ascii_value = ord(char)
    q_score = ascii_value - 33
	
    return 10 ** (-q_score / 10)
    
def prob_to_char(prob):
    
    q_score = -10 *math.log10(prob)
    ascii_value = int(round(q_score)) + 33
    
    return chr(ascii_value)
    
print(char_to_prob('A'))
print(prob_to_char(0.001))
