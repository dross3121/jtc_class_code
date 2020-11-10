'''
Planning challenge 2!

For each piece here, write out the pseudocode as comments FIRST, then write your code!
'''


'''
1. Shipping

You are building a system to handle shipping orders. Each order should be a dictionary that has 3 pieces of information:
-destination (string) (for the purposes of this challenge this can be any place, no need to make a full address)
-date_shipped (string)
-weight (float) (how many pounds the package is)

Assign 3 separate orders to 3 separate variables
'''
print('\nPART 1')
# make a dictionary with these values
# "New York" 'Oct.29' "2.0"
# "Baltimore" "Sept.24" "10.0"
# "Seattle" "Jan.1" "12.5"
order1 ={'destination': "New york", 'date_shipped': "oct.29", 'weight': 2.0 }
order2 = {'destination': "Baltimore", 'date_shipped': "sept.24", 'weight': 10.0}
order3 = {'destination': "Seattle", 'date_shipped': "Jan.1", 'weight': 12.5}

# print(order3)


'''
2. Building the database

Now, let's put the orders all into a database togther (all the orders are storedin 1 variable). 

Your database can either be a dictionary or a list. 

Print out the database to make sure all the info is in there. 

'''
print('\nPART 2')
# create a list to store variables/dicts
shipped_items = [order1, order2, order3]
# print(shipped_items)

'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''
print('\nPART 3')
# create func. named add_order() to add new order to list
#add 1 new dict to list
order4 = {'destination': "Boise", 'date_shipped': "Jan.31", 'weight': 31.50} 
def add_order(order):
	
	shipped_items.append(order4)


add_order(order4)
print(shipped_items)

'''
4. Define a function called complete_order() to mark a specific order in your database complete

This means that it should add a new key/value pair called 'complete' to a specific order, and set the value to True

Test this out and print out your database to make sure it works!

HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database
'''
print('\nPART 4')

# define func complete_order
# add new key/value pair 
# set key: complete value: true

def complete_order(order_index):
	 shipped_items[order_index]["complete"]= True

complete_order(0)
print(shipped_items)