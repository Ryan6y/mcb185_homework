import sys
import gzip
import json

def read_transfac(filepath):
    records = []
    current_record = None
    
    opener = gzip.open if filepath.endswith('.gz') else open
    with opener(filepath, 'rt') as fp:
        for line in fp:
            line = line.strip()

            if not line:
                continue
                
            if line.startswith('ID'):
                if current_record:  
                    records.append(current_record)
                current_record = {
                    'id': line.split()[1],
                    'pwm': []
                }
                
            elif line[0].isdigit():
                fields = line.split()
                if len(fields) >= 5:  
                    pos_data = {
                        'A': float(fields[1]),
                        'C': float(fields[2]),
                        'G': float(fields[3]),
                        'T': float(fields[4])
                    }
                    current_record['pwm'].append(pos_data)

            elif line.startswith('//'):
                if current_record:
                    records.append(current_record)
                current_record = None
                
        if current_record:
            records.append(current_record)
            
    return records

filepath = sys.argv[1]
records = read_transfac(filepath)

print(json.dumps(records, indent=4))

