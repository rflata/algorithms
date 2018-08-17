aa = {
'TTT':'F',
'TTC':'F',
'TTA':'L',
'TTG':'L',
'TCT':'S',
'TCC':'S',
'TCA':'S',
'TCG':'S',
'TAT':'Y',
'TAC':'Y',
'TAA':'Stop',
'TAG':'Stop',
'TGT':'C',
'TGC':'C',
'TGA':'Stop',
'TGG':'W',
'CTT':'L',
'CTC':'L',
'CTA':'L',
'CTG':'L',
'CCT':'P',
'CCC':'P',
'CCA':'P',
'CCG':'P',
'CAT':'H',
'CAC':'H',
'CAA':'Q',
'CAG':'Q',
'CGT':'R',
'CGC':'R',
'CGA':'R',
'CGG':'R',
'ATT':'I',
'ATC':'I',
'ATA':'I',
'ATG':'M',
'ACT':'T',
'ACC':'T',
'ACA':'T',
'ACG':'T',
'AAT':'N',
'AAC':'N',
'AAA':'K',
'AAG':'K',
'AGT':'S',
'AGC':'S',
'AGA':'R',
'AGG':'R',
'GTT':'V',
'GTC':'V',
'GTA':'V',
'GTG':'V',
'GCT':'A',
'GCC':'A',
'GCA':'A',
'GCG':'A',
'GAT':'D',
'GAC':'D',
'GAA':'E',
'GAG':'E',
'GGT':'G',
'GGC':'G',
'GGA':'G',
'GGG':'G'
}
complement = {'A':'T','T':'A','G':'C','C':'G'}
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

def revcomp(dna):
	rev = ''
	for b in dna:
		rev += complement[b]
	rev = rev[::-1]
	return (rev)

def translate(dna):
	polypep = []
	for i in range(3):
		poly = ''
		ORF = 0
		for j in range(i, len(dna), 3):
			if (aa.get(dna[j:(j+3)]) == 'M'):
				ORF = 1
			if (aa.get(dna[j:(j+3)]) == 'Stop'):
				ORF = 0
				start = []
				for i,c in enumerate(poly):
					if c == 'M':
						start.append(i)
					if (len(poly) > 0):
						for n in start:
							if poly[n:len(poly)] not in polypep:
								polypep.append(poly[n:len(poly)])
				poly = ''
			if ORF == 1:
				poly = poly + (aa.get(dna[j:(j+3)]))
	return polypep

dna = readGenome('fasta.txt')
dnas = []
orfs = []
dnas.append(dna)
dnas.append(revcomp(dna))

for na in dnas:
	orfs.append(translate(na))
mergedorfs = []
for list in orfs:
	for item in list:
		if item not in mergedorfs:
			mergedorfs.append(item)

for item in mergedorfs:
	print(item)
