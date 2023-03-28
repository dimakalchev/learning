# name_char = len(input("What is your name?\n"))
# new_name_char = str(name_char)
# print("Your name has " + new_name_char + " characters")




# three_digit_number = input("Type a three digit numder: ")
# first_digit_number = three_digit_number[0]
# second_digit_number = three_digit_number[1]
# third_digit = three_digit_number[2]

# result = int(first_digit_number) + int(second_digit_number) + int(third_digit)

# print(result)

# ** = stepen'
# PEMDAS
#  ()              parenthesis
#   **             exponents
#   *              multiplication
#   /              division
#   +              addition 
#   -              subtraction
# print(3 * (3 + 3) / 3 - 3)




# height = input("Enter your height in m: ")
# weight = input("Enter your weight in kg: ")
# BMI = float(weight) / float(height) ** 2


# print(int(weight) / float(height) ** 2)
# bmi_as_int = int(BMI)
# print(bmi_as_int)

# // = integer
# print(4 / 2)
# result = 4 // 2
# print(result)
# score = 2
# score **=3
# height = 1.79
# print(score)
# # f-String
# print(f"your score is {score}, your height is {height}")

# CODING EXERSICE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# age = input("What is your current age? ")
# years = 90 - int(age)
# months = years * 12
# weeks = years * 52
# days = years * 365
# message = f"You have {days} days, {weeks} weeks, {months} months and {years} years until 90 years"
# print(message)


# PROJECT TIP CALCULATOR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

print("Welcome to the tip calculator!")
sum = input("What was the total bill? $")
sum_as_float = float(sum)
tip_pers = input("What percentage tip would you like to give? 10, 12, or 15?" )
tip_pers_as_float = int(tip_pers)
common_sum_as_float = int(tip_pers_as_float / 100 * sum_as_float + sum_as_float)
persons = input("How many people to split the bill? ")
persons_as_int = int(persons)
each_person = common_sum_as_float / persons_as_int
sum_of_tips = common_sum_as_float - sum_as_float
each_persons_tip = int(sum_of_tips / persons_as_int)
final_amount = round(each_person, 2)
final_amount = "{:.2f}".format(each_person, 2)
print(f"Final amount is {common_sum_as_float} $")
print(f"Tips are {sum_of_tips} $")
print(f"Each person's tip is {each_persons_tip} $")
print(f"Each person should pay: {final_amount} $")
