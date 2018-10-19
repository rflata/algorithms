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
'TAA':'',
'TAG':'',
'TGT':'C',
'TGC':'C',
'TGA':'',
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
def splice(dna, introns):
    for intron in introns:
        dna = dna.replace(intron,'')
    return(dna)

def translate(dna):
    polypep = ''
    for i in range(0, len(dna), 3):
        polypep = polypep + aa[dna[i:i+3]]
    return(polypep)
a = []
genome = ''
with open('fasta.txt') as fasta:
	for line in fasta:
		if not line[0] == '>':
			genome += line.rstrip()
		else:
			if (len(genome) > 0):
				a.append(genome)
				genome = ''
a.append(genome)
dna = a[0]
introns = a[1:]
spliced = splice(dna, introns)
print(translate(spliced))

