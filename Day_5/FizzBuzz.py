# for n in range(1, 11, 3):
#     print(n)
# total = 0
# for number in range (0, 101, 2):
#     total += number
# print(total)
#
# total = 0
# for number in range ( 1, 101, 2):
#     total = total + number + 1
# print(total)

# total2 = 0
# for number in range(1, 101):
#     if number % 2 ==0:
#         total2 += number
# print(total2)



# FizzBazz Game
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
