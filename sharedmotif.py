import time
genome = ''
genomes = []

with open('fasta.txt') as fasta:
	for line in fasta:
		if not line[0] == '>':
			genome += line.rstrip()
		else:
			if (len(genome) > 0):
				genomes.append(genome)
				genome = ''
genomes.append(genome)
substrings = []
start = time.time()
for i, b in enumerate(genomes[0]):
	for j, n in enumerate(genomes[1]):
		if b == n:
			sub1 = genomes[0][i:]
			sub2 = genomes[1][j:]
			k = 0
			substring = ''
			while sub1[k] == sub2[k] and (k < len(sub1)-1 and k < len(sub2)-1):
				substring = substring + sub1[k]
				substrings.append(substring)
				k += 1
substrings = sorted(substrings, key=len, reverse=True)
end = time.time()
print(end-start)
start = time.time()
for i in range(2, len(genomes)):
	for n,j in enumerate(substrings):
		if j in genomes[i]:
			substrings = substrings[n:]
			break
end = time.time()
print(end-start)
print(substrings[0])