def tm(a, c, g, t):
  length = a + c + g + t
	
  if length <= 13:
    tm= (a + t) * 2 + (g + c) * 4 #for short
  else:
    tm = 64.9 + 41 * (g + c - 16.4) / length #for long
  return tm

print(tm(5, 7, 3, 4))
