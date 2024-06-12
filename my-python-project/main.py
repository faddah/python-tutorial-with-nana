import sys

# Built-in Python Functions

print("So long, suckerz!")
input("Press enter to exit!")
print(set([1, 3, 4]))
print(int("20"))
print("2, 3".split(", "))
print("text".split())
print([1, 2, 3].count(1))



calculation_to_units = 24 * 60 * 60
name_of_unit = "seconds"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    if num_of_days_element == "exit" or num_of_days_element == "quit":
        print("Exiting the program")
        sys.exit()
    try:
        user_input_number = int(num_of_days_element)

        # we want to do conversion only for positive integers
        if user_input_number > 0:
            #calculated_value = days_to_units(user_input_number)
            print(days_to_units(user_input_number))
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negative number, no conversion for you!")
    except ValueError:
        print("your input is not a valid number. Don't ruin my program!")


user_input = ""
while user_input != "exit" or user_input != "quit":
    user_input = input("Hey user, enter number of days as a comma separated list and I will convert it to hours!\n")
    list_of_days = user_input.split(", ")
    for num_of_days_element in set(list_of_days):
        validate_and_execute()
