import sys


   

# Built-in Python Functions

print("So long, suckerz!")
input("Press enter to exit!")
print(set([1, 3, 4]))
print(int("20"))
print("2, 3".split(", "))
print("text".split())
print([1, 2, 3].count(1))

# print('Number of Mintues in 20 Days:', 20 * 60 * 24)
calculate_days_to_seconds = 60 * 60 * 24
name_of_units = 'seconds'


def days_to_units(num_of_days):
    return print(f"{num_of_days} Days are {num_of_days * calculate_days_to_seconds} {name_of_units}. ")
 
 
 
def validate_and_execute(num_of_days_element):
    if num_of_days_element == 'exit' or num_of_days_element == 'quit':
        print("So long, suckerz!")
        sys.exit()
    try:
        user_input_number = int(num_of_days_element)
        # we want to do conversion only for positive ingtegers 
        if user_input_number > 0:
            days_to_units(user_input_number)
            # print(calculation)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number!")
        else:
            print("You entered a negative number. No conversion for you!")
    except ValueError:
        print("You entered an invalid input. Don't ruin my program!")
   


USER_INPUT = ''
while USER_INPUT != 'exit' or USER_INPUT != 'quit':
    USER_INPUT = input("Hey user, enter the number of days as a comma separated list and I will convert it to hours!\n\n")
    list_of_days = USER_INPUT.split(",")
    """print(list_of_days)
    print(set(list_of_days))
    print(type(list_of_days))
    print(type(set(list_of_days)))"""
    for num_day_element in set(USER_INPUT.split(", ")):
        validate_and_execute(num_day_element)
