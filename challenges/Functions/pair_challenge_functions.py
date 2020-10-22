def create_account():
	username = input(f'Please type username: ')
	password = input(f'Please type password: ')
	balance = float(0)
	user_bank = {'username': username, 'password': password, 'balance': balance}
	return user_bank

def deposit(account, amount):
	account['balance'] += amount


def withdraw(account, amount):
	if account['balance'] >= amount:
		account['balance'] -= amount
	else: 
		print("Not enough avaiable funds")

