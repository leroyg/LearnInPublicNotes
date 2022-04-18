# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆 It's only for testing your code.

# Write the rest of your code below this line 👇

heads_or_tails = random.randint(0, 1)


def coinflip():
    user_choice = input("Do you want to flip a coin? Y or N\n")
    user_choice = user_choice.lower()
    if user_choice == "y":
        if heads_or_tails == 1:
            user_choice = "Heads"
        elif heads_or_tails == 0:
            user_choice = "Tails"
        print(user_choice)
    else:
        print("No worries come back later when you can play.")


coinflip()


# #Remember to use the random module
# #Hint: Remember to import the random module here at the top of the file. 🎲
# import random
# # 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
#  # 🚨 Don't change the code above 👆 It's only for testing your code.

# #Write the rest of your code below this line 👇
# heads_or_tails = random.randint(0, 1)
# def coinflip():
#         if heads_or_tails == 1:
#             print("Heads")
#         elif heads_or_tails == 0:
#             print("Tails")

# coinflip()
