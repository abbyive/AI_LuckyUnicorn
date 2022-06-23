# ask the user if they have played before
show_instructions = input("Have you played this game before? ").lower()

# if they say yes, output 'program continues'
# if they say anything else, send 'error'
# if they say no, output 'display instructions'
if show_instructions == "yes":
    print("program continues")

elif show_instructions == "y":
    print("program continues")

elif show_instructions == "no":
    print("display instructions")

elif show_instructions == "n":
    print("display instructions")

else:
    print("Sorry, that is not a valid response. Please answer with 'yes' or 'no'.")
