import itertools as it

prod = list(it.product('ABCDEFG', repeat=3))
for value in prod:
	print(''.join(value))