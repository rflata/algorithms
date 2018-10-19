complement = {'A':'T','T':'A','G':'C','C':'G'}
sites = []
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

def comp(dna):
    comp = ''
    for base in dna:
        comp = comp + complement[base]
    return comp[::-1]

dna = readGenome('fasta.txt')
for i, base in enumerate(dna):
    dnastring = base
    for bp in dna[(i + 1):]:
        dnastring = dnastring + bp
        if(len(dnastring) > 12):
            break
        if((dnastring == comp(dnastring)) and (len(dnastring) > 3)):
            sites.append(str(i+1) + '\t' + str(len(dnastring)))
for site in sites:
    print(site)