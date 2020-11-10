# Intro to Programming Using Python - Assignment #1# Completed by:
# 1. Print out the following text: 
# On lines 4 & 5 im using the print() function to display the following two statements
print("You've reached Deshawn Ross.") 
print("I'm not available right now, so leave a message and I'll call you back.")


# 2. Create five variables for your first name, last name, shoe size, height, and age. # And then print them out on one line.

#  im creating variables to for first name, last name, shoe size, height, and age and then using the print() function to display  the variables
first_name = 'Deshawn'
last_name = 'Ross,'
shoe_size = 'Shoe size:10.5,'
height = "Height:5'11,"
age = 'Age:31'
print(first_name, last_name, shoe_size, height, age)


# 3. If subtotal = 10.58 and tip = 0.22 (22%) then calculate the total bill amount# in a variable named total and print it out.
# creating variables for subtotal and tip of a bill, then concatenating the two variables in the "total" variable using the (+) to get the final bill total, finally im using the print() function to display the total
subtotal = 10.58
tip = 0.22
total = subtotal + subtotal*tip 
print(total)

# 4 Convert 158.8 into an integer. 
# converting 158.8 from a float to a integer using the int() function 
print(int(158.8))
# Convert 75 into a float. 
# converting 75 from an integer to float using the float() function
print(float(75))
# Convert "244.9" into a float and then an integer.
# converting "244.9" from a str to a float then turning that float into an integer
print(int(float("244.9")))

# 5. Use \t and \n in a string and then print it out so that it matches (approximately) the following:# -in the woods#               which#                   stutter#                           and# #                               sing
print('-in the woods             \n\t\twhich              \n\t\t\tstutter                          \n\t\t\t\tand                              \n\t\t\t\t\tsing')

# 6. Put your first name and total from above into an f-string (f"...") so that it reads: # Mattan, your total is $12.91 # (remember to round the total to the nearest cent)
# for the following code i am using an f-string to display the following "Deshawn your total is $10.80" 
print(f"{first_name}, your total is ${total:.2f}")

# 7. Use input() to ask a user for the city they live in, and then print it back tothem.
# using and input statement to ask the user "What city do they live in? then printing that input backto the user"
print(input("What city do you live in? "))

# print(f'{city} is a great city!')


# 8. Build a future value calculator by using input() to get values from the user. # (Make sure you convert them into integers or floats before doing any math on them.) # Print out the result.# Hint: Future Value = Present Value x (1 + rate of return) ^ number of periods

def pay_my_weight():
	Present_value = float(input('How much do you owe the bank? '))
	rate_of_return = float(input('What is your rate of return? '))
	number_of_periods = float(input("How many months is your loan? "))
	Future_Value = Present_value * (1 + rate_of_return) ** number_of_periods
	return Future_Value
	

print(input(f'You owe {pay_my_weight()}.'))	
	