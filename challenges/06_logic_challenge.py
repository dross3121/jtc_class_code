print("Challenge 3.1: Debug code snippets")

print()

print("Code Snippet 1:")

a = 1
b = 1
c = (a > b)

print("The value of c is False since a isn't greater than b.")

print()

print("Code Snippet 2:")

d = (True or (5 > 7) or not (8 < 20))

print("The value of d is True since 5 is not greater than 7.")

print()


print("Code Snippet 3:")

m = "GOAT"
n = "goat"

o = (m == n)

print ("The value of o is False since Python is case-sensitive.")

print()

print("Code Snippet 4:")

u = 5
v = 2

if u * v == 10:
    print("The product of a and b is 10")
else:
    print("The product of a and b is not 10") 

print()

print("Code Snippet 5:")
x = 15
y = 25

z = 30

if z < x:
    print("z is less than x")

elif z > x and z < y:
    print("z is between x and y")

else:
    print("z is greater than y")


print()
print()
print()

print("Challenge 3.2: Playing with the stock market")

print()

print("Challenge 3.2.1: Creating variables")
# Create variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
Apple = 100
Facebook = 250
Google = 1400
Microsoft = 200
print()


print("Challenge 3.2.2: Taking user input")
name = input("What is your name?")

savings = int(input("What is your savings amount?"))


# TODO: Write code to ask the client his name and save it to a variable.
# TODO: Write code to ask the client his savings and save it to another variable.
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.3: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

'''
Your code should look like this:

if stock == "amzn":
    ...

elif ...
else ...
# '''
if stock == "amzn":
	print(int(savings/amazon))

elif stock == "aapl":
	print(int(savings/Apple))

elif stock == "msft":
	print(int(savings/Microsoft))

elif stock == "goog":	
	print(int(savings/Google))

elif stock == "fb":
	print(int(savings/Facebook))






print()

print("Challenge 3.2.4: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print("Shawn has $30000 in savings he can buy 10 shares of Amazon at the current price of $3000.")