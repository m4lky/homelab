#!/usr/bin/python3
# the shebang above tells the system which environment to run in

# this is asking user for their age
age = input("Enter your age: ")
# this takes the age and converts it to an integer
age = int(age)

# if statements to figure out which output to give
if age >= 21:
    print ("You are old enough to drink in America")
elif age >= 18:
    print ("You are old enough to drink in UK")
elif age < 18:
    print ("Get out you underage cunt")
