# *************** functions go here ********************

# *************** main routine goes here ****************

error = "Please enter a whole number between 1 and 10 \n"

valid = False
while not valid:
    try:
        # ask the question
        response = int(input("How much money would you like to play with? $"))
        # if amount is too low/high give
        if 0 < response <= 10:
            print("You have asked to play with ${}.".format(response))
        # print an error
        else:
            print(error)
    except ValueError:
        print(error)
