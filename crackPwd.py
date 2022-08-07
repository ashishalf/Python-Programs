import random
import string

your_pass = input("Enter your password: ")

pwd = string.ascii_lowercase

guess = ""
while(guess != your_pass):
    guess = ""
    for letter in range(len(your_pass)):
        g_letter = pwd[random.randint(0, 25)]
        guess = str(g_letter)+str(guess)

    print(guess)

print('Your Guess Password: ', guess)
