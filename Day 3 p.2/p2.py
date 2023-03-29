# 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

# height = int(input("What is your height? "))
# bill = 0
#
# if height > 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print(f"Your bill is {bill} $")
#     elif age < 18:
#         bill = 7
#         print(f"Your bill is {bill} $")
#     elif age < 45 or age > 55:
#         bill = 12
#         print(f"Your bill is {bill} $")
#     else:
#         print(f"Your bill is {bill} $")
#
#     photo = input("Do you want photo? Y or N ")
#     if photo == "Y":
#         bill += 3
#         print(f"Your final bill is {bill} $")
#     if photo == "N":
#         print(f"Your final bill is {bill} $")
# else:
#     print("Sorry, you can`t go rollercoaster")


print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
lower_name1 = name1.lower()
lower_name2 = name2.lower()
t = lower_name1.count("t") + lower_name2.count("t")
r = lower_name1.count("r") + lower_name2.count("r")
u = lower_name1.count("u") + lower_name2.count("u")
e = lower_name1.count("e") + lower_name2.count("e")
true = str(t + r + u + e)
l = lower_name1.count("l") + lower_name2.count("l")
o = lower_name1.count("o") + lower_name2.count("o")
v = lower_name1.count("v") + lower_name2.count("v")
e = lower_name1.count("e") + lower_name2.count("e")
love = str(l + o + v + e)
love_score = int(true + love)

if love_score <= 10 or love_score >= 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}, you can be together")





























