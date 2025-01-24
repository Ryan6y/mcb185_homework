# 12ohred.py by Xiaoran Yu

import math

def char_to_prob(char):
    
    if not isinstance(char, str) or len(char) != 1:
    	return None
    	
    ascii_value = ord(char)
    q_score = ascii_value - 33
	
    if q_score < 0:
    	return None
    
    return 10 ** (-q_score / 10)
    
def prob_to_char(prob):
    
    if not isinstance(prob, (int, float)) or prob <=0 or prob >=1:
    	return None
    
    q_score = -10 *math.log10(prob)
    ascii_value = int(round(q_score)) + 33
    
    if ascii_value < 33 or ascii_value >126:
    	return None
    
    return chr(ascii_value)
    
print(char_to_prob('A'))
print(prob_to_char(0.001))
