def fib(n, m):
	c = 0
	a, b = 1, 1
	mem = [a,b]
	for i in range(2, n):
		if i < m:
			a, b = b, a + b
			mem.append(a)
		else:
			a, b = b, (a + b - mem[c])
			mem.append(a)
			c += 1
	return b
print(fib(96,18))