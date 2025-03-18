import sys

def dtc(P, Q):
    d = 0
    for p, q in zip(P, Q):
        d += abs(p - q)
    return d

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
input_color = (R, G, B)

min_dis = 0
closest_color = 0

with open(colorfile, 'rt') as fp:
    for line in fp:
        
        line = line.strip()
        parts = line.split()
        name = parts[0]
        rgb_code = parts[2].split(',')
        
        r = int(rgb_code[0])
        g = int(rgb_code[1])
        b = int(rgb_code[2])
        
        color_value = (r, g, b)
        dis = dtc(input_color, color_value)
        
        if min_dis == 0 or dis < min_dis:
            min_dis = dis
            closest_color = name

print(closest_color)