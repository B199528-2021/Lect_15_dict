#!/usr/local/bin/python3

import os
import sys
import subprocess
import shutil

userinput={}

userinput["name"] = input("\nWhat's your name? > ")
print("Cool name")

while True:
    try:
        checkage = int(input("\nHow old are you? > "))
    except ValueError:
        print("Please type in a number.")
        continue
    if checkage > 18 and checkage < 25:
        print("You are not old.")
    if checkage <= 18:
        print("You are very young.")
    else:
        print("Don't think that you are old!")
    print("Thanks for letting me know.")
    userinput["age"] = checkage
    break

colourcheck = input("\nWhat is your favourite colour? > ")
if colourcheck == "blue":
    print("We have the same favourite colour.")
else:
    print("Your favourite colour is interesting.")
userinput["colour"] = colourcheck

while True:
    worldcheck = input("\nDo you think the world is flat? > ").lower()
    while worldcheck not in ("yes", "y", "no", "n"):
        worldcheck = input("Please type in 'yes'/'y' or 'no'/'n' > ").lower()
    if worldcheck == "yes" or worldcheck == "y":
        userinput["flatworld"] = True
        print("I didn't know that.")
        break
    else:
        userinput["flatworld"] = False
        print("That's boring.")
        break

print(f"\nThis is the dictionary about you:\n{userinput}")


