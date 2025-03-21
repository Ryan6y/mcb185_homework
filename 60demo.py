d = [
    'hello',
    (3.14, 'pi'),
    [-1, 0, 1],
    {'year': 2000, 'month': 7}
]
print(d[0][4], d[1][0], d[2][2], d[3]['month'])

oligo = {
    'Name': 'SO116',
    'Length': 18,
    'Sequence': 'ATTTAGGTGACACTATAG',
    'Description': 'SP6 promoter sequencing primer'
}

def read_catalog(filepath):
    catalog = []
    with open(filepath) as fp:
        for line in fp:
            if line.startswith('#'): continue
            name, length, seq, desc = line.rstrip().split(',')
            record = {
                'Name': name,
                'Length': length,
                'Sequence': seq,
                'Description': desc
            }
            catalog.append(record)
    return catalog