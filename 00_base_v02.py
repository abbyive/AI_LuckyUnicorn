"""

base component for the game Lucky Unicorn
V01 - instructions + yes/no checker

author - Abby Ives
CC AVI 2022

"""

# import libraries below this line ****************************************


# all functions below this line ********************************************
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please enter either 'Yes' or 'No'.")


def instructions():
    print("***** How To Play *****")
    print()
    print("The rules of the game go here")
    print()
    return""


def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10 \n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if amount is too low/high give
            if low < response <= high:
                return response
            # print an error
            else:
                print(error)
        except ValueError:
            print(error)


# print main routine below this line *************************************
played_before = yes_no("Have you played the game before? ")
if played_before == "no":
    instructions()

# ask how much money they want to play with
how_much = num_check("How much would you like to play with? ", 0, 10)
print("You will be spending ${}".format(how_much))
