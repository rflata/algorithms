samples = []
genome = ''
genomes = []
with open('fasta.txt') as fasta:
	for line in fasta:
		if line[0] == '>':
			samples.append(line.strip('>').rstrip())
		if not line[0] == '>':
			genome += line.rstrip()
		else:
			if (len(genome) > 0):
				genomes.append(list(genome))
				genome = ''
genomes.append(list(genome))
print(samples)
for i in range(len(samples)):
	for j in range(len(samples)):
		if ((genomes[i] != genomes[j]) and (genomes[i][0:3] == genomes[j][(len(genomes[j])-3):(len(genomes[j]))])):
			print(samples[j] + ' ' + samples[i])