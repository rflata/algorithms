
x = "3141592653589793238462643383279502884197169399375105820974944592"
y = "2718281828459045235360287471352662497757247093699959574966967627"

a = x[:(len(x)//2)]
print("a = " + a)
b = x[(len(x)//2):]
print("b = " + b)
c = y[:(len(y)//2)]
print("c = " + c)
d = y[(len(y)//2):]
print("d = " + d)

karatsuba = ((10**len(x))*(int(a)*int(c)))+(10**(len(x)//2))*((int(a)*int(d))+(int(b)*int(c)))+(int(b)*int(d))

print(karatsuba)