print('Question 1')
# You're starting a deli and your supplier currently provides with these ingredients
meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

# You want to create a menu soon, but first things first...
# TODO: Let's capitalize the first letter of each word in each list using .capitalize()

# loop for to add index for the meats
for i in range(len(meats)):
# reassigning each meat with the captitalized version
	meats[i] = meats[i].capitalize() 
	# print(i)
print(meats)
for dog in range(len(cheeses)):
	cheeses[dog] = cheeses[dog].capitalize()
	# print(dog)
print(cheeses)	

print('Question 2')
# Great! Your lists look much better. You need to come up with every combination of meats and cheeses for your menu.
# TODO: Use nested loops to create every combination of meat and cheese and add it to the sandwiches list
sandwiches = []
for i in meats:
	for dog in cheeses:
		print(i + "&" + dog)

		sandwiches.append(i + "&" + dog)

		

print(sandwiches)

print('Question 3')
# TODO: Let's create an input to take a customer order for a sandwich, for example: 'Ham & Swiss'
# TODO: Loop over the sandwiches list.
# TODO: If it exists, print 'Great choice! 1 Ham & Swiss coming right up!'
print('Great choice! 1 Ham & Swiss coming right up!')
