import sys

print('Number of Mintues in 20 Days:', 20 * 60 * 24)
# print(False)
calculate_days_to_seconds = 60 * 60 * 24
name_of_units = 'seconds'


def days_to_units(num_of_days):
		#print(custom_message)
		# print(num_of_days > 0)
		# conditional_check = num_of_days > 0
		# print(type(conditional_check))
		return print(f"{num_of_days} Days are {num_of_days * calculate_days_to_seconds} {name_of_units}. ")
 
 
def validate_and_execute():
	try:
		user_input = int(num_of_days_element)
		# we want to do conversion only for positi ve ingtegers 
		if user_input > 0:
			calculate_days_to_seconds = days_to_units(user_input)
			print(calculate_days_to_seconds)
		elif user_input == 0:
			print("You entered a 0, please enter a valid positive number!")
		else:
			print("You entered a negative number. No conversion for you!")
	except ValueError:
		# if user_input == 'exit' or user_input == 'quit':
		# 	print("Exiting the program!")
		# 	sys.exit()
		# else:
		print("You entered an invalid input. Don't ruin my program!")
   
   

# def scope_check(num_of_days=20):
# 	print(name_of_units)
# 	print(f"num_of_days = {num_of_days}")  # This will throw an error because num_of_days is not defined in this scope.


# scope_check()

# print("5 Days are " + str(5 * calculate_days_to_seconds) + " " + str(name_of_units) + ".")
# print("15 Days are " + str(15 * calculate_days_to_seconds) + " " + str(name_of_units) + ".")
# msg = "All Good!"
# days_to_units(20, msg)
# days_to_units(35, msg)
# days_to_units(50, msg)
# days_to_units(110, msg)
# days_to_units(150, msg)

# print(f"20 Days are {2020 * calculate_days_to_seconds} {name_of_units}. ")
# print(f"35 Days are {3520 * calculate_days_to_seconds} {name_of_units}. ")
# print(f"50 Days are {5020 * calculate_days_to_seconds} {name_of_units}. ")
# print(f"110 Days are {11020 * calculate_days_to_seconds} {name_of_units}. ")

# my_var = days_to_units(20)
# print(my_var)

#user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
# print(user_input)
user_input = ''
while user_input != 'exit' or user_input != 'quit':
	user_input = input("Hey user, enter a number of days as a comma separated list and I will convert it to hours!\n")
	list_of_days = user_input.split(', ')
	print(list_of_days)
	print(set(list_of_days))
	print(type(list_of_days))
	print(type(set(list_of_days)))
	for num_of_days_element in set(list_of_days):
		validate_and_execute()


print(type(True))
print(type("this should be a string"))
print(type(30))
print(type(30.99))
