# import sys

# print('Number of Mintues in 20 Days:', 20 * 60 * 24)
calculate_days_to_seconds = 60 * 60 * 24
name_of_units = 'seconds'


def days_to_units(num_of_days):
    return print(f"{num_of_days} Days are {num_of_days * calculate_days_to_seconds} {name_of_units}. ")
 
 
 
def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        # we want to do conversion only for positive ingtegers 
        if user_input_number > 0:
            calculation = days_to_units(user_input)
            print(calculation)
        elif user_input == 0:
            print("You entered a 0, please enter a valid positive number!")
        else:
            print("You entered a negative number. No conversion for you!")
    except ValueError:
        print("You entered an invalid input. Don't ruin my program!")
   


user_input = ''
while user_input != 'exit':
    user_input = input("Hey user, enter the number of days as a comma separated list and I will convert it to hours!\n")
    """print(type(user_input.split(", ")))
    print(user_input.split(", "))"""
    for num_of_days_element in user_input.split(", "):
        validate_and_execute()
   


