
def pay_my_weight():
	Present_value = float(input('How much do you owe the bank? '))
	rate_of_return = .20
	number_of_periods = 12
	Future_Value = Present_value * (1 + rate_of_return) ** number_of_periods
	return Future_Value

print(f'You really owe the bank {pay_my_weight()}')	