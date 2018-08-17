balance = 320000
annualInterestRate = 0.2
mintrate = (annualInterestRate/12)
lower = balance/12
#print(lower)
upper = (balance*((1+mintrate)**12))/12.0
#print(upper)

while True:
	bal = balance
	#print("Low: " + str(lower) + " High: " + str(upper))
	mpay = (lower + upper)/2
	#print("Payment: " + str(mpay))
	for x in range(12):
		#pay = mpayrate * bal
		bal = bal - mpay
		bal = bal + (mintrate * bal)
	#print("Balance: " + str(bal))
	if round(bal) == 0:
		break
	elif bal > 0:
		lower = mpay
		
	elif bal < 0:
		upper = mpay
print("Lowest Payment: " + str(round(mpay,2)))