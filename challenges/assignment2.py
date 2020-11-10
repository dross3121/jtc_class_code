# Intro to Programming Using Python - Assignment #2
# Completed by: 

# 1. Write an if statement that checks if user is "mattangriffel"
# and prints out "Welcome professor" if so, or "Who are you?" if not.

user = "mattangriffel"
# user = "DeshawnRoss"

if user == "mattangriffel":
	print("Welcome professor")
else:
	print("Who are you?")

# 2. Write an if statement that checks both the credentials below
# and prints "Successfully logged in." if they're correct or
# "Invalid username/password combination. Try again." if they're not.

user = "mattangriffel"
password = "123456"
# user = "deshawn"
# password = "123456"

if user == "mattangriffel" and password == "123456":
		print("Successfully logged in")
else:
	print("Invalid username/password combination. Try again.")		


# 3. Write an if statement that checks whether the value of number is divisible
# by two and prints out "even" if it is and "odd" if it's not.
# (Hint: You can check divisiblity using the modulus (%) operator. 
# n % k == 0 evaluates to true if n is an exact multiple of k.)

number = 4
# number = 99

if number % 2 == 0:
	print("even")
else:		
	print("odd")


# 4. Create three different lists containing:
# - The names of all your siblings
# - Your top 3 favorite movies
# - The latitude and longitude coordinates of Columbia University
family = ["Charli", "Deshawn", "Kay", "Mom", 'Deandre', "Joseph", 'Monica', "Darrin", "Takasha"]
fav_movies = ["Guardians of the Galaxy", "The Wood", "Eddie Murphy Delirious"]
ColumbiaU_lat_long = ["40.80819° N", "-73.958305° E"]

# 5. Use a for loop on each of the lists above to print out each element on its own line.
for members in family:
	print(members)
for movies in fav_movies:
	print(movies)
for location in ColumbiaU_lat_long:
	print(location)
# 6. Use a for loop and the title() function to print out each city name capitalized

cities = ["new york city", "san francisco", "boston", "chicago", "los angeles"]

for name in cities:
	print(name.title())
# 7. A list is different from an element in a list.  What's something you can do
# to the second in Python that you can't do to the first, and vice versa?

person = ["Mattan"]
#  Can call an element in a list by index[0][1][2] because list are ordered.
# you can loop through list 
person = "Mattan"
# while a string doesn't have any elements, per se, you can still loop through the characters in a string and get them by index.

# 8. Use range() and a for loop to print out:
# - the numbers from 1 to 10
# - the square of each of the numbers from 1 to 10
# - for each number from 1 to 10, print out whether it is even or not

for nums in range(1,11):
	print(nums)
	print(nums**2)
	if nums % 2 == 0:
			print("even")
	else:
		print("odd")




# Bonus: In Mathematics, a Marsenne number is a number that is one less than a
# power of two (i.e. 2^n - 1). Starting with an empty list named 
# marsenne_numbers (provided for you below),  use the append() function inside
# of a for loop so that after the loop has run, marsenne_numbers contains a
# list of the first ten Marsenne numbers.

marsenne_numbers = []

for marsenne in range(1,11): 
	nums = (2**marsenne) - 1
	marsenne_numbers.append(nums)


print(marsenne_numbers)