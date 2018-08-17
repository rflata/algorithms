import pandas as pd
genome = ''
a = []
b = []
string = ''
with open('fasta.txt') as fasta:
	for line in fasta:
		if not line[0] == '>':
			genome += line.rstrip()
		else:
			if (len(genome) > 0):
				a.append(list(genome))
				genome = ''
a.append(list(genome))

df = pd.DataFrame(a)
df2 = pd.DataFrame()
for column in df:
	b.append(df[column].value_counts().to_frame())
#print(b)
c = pd.concat(b, axis=1, sort = True)
c.fillna(0, inplace=True)
c = c.apply(pd.to_numeric, downcast='integer')
for column in c:
	string = string + c[column].idxmax()
print(string)
print(c)
with open('output.txt', 'w') as out:
	out.write(string + '\n')

c.to_csv('output.txt', sep=' ', mode= 'a')
