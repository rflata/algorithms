def balance(balance,aintrate,mpayrate):
	mintrate = (aintrate/12)
	
	for x in range(12):
		minpay = mpayrate * balance
		unpaid = balance - minpay
		balance = unpaid + (mintrate * unpaid)
		
		#month = x + 1
		#r = (round(balance,2))
		#print("Month " + str(x+1) + " Remainging balance: " + str(r))
	return(balance)
balance = balance(42, 0.2, 0.04)
print("Remaining balance: " + str(round(balance,2)))

