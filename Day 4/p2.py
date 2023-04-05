
# names_string = input("Give me everybody's names, separated by a comma ")
# names = names_string.split(", ")
# print(names)
#
#
# import random
# random_name = random.randint(0, len(names) - 1)
# print(names[random_name] + " is going to buy the meal today")


# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)


#
# row1 = ["⬜", "⬜", "⬜"]
# row2 = ["⬜", "⬜", "⬜"]
# row3 = ["⬜", "⬜", "⬜"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = int(input("Where do you want to put the treasure? "))
# len(row1)
# if position == 11:
#     row1 = ["X", "⬜", "⬜"]
#     print(f"{row1}\n{row2}\n{row3}")
# if position == 12:
#     row2 = ["X", "⬜", "⬜"]
#     print(f"{row1}\n{row2}\n{row3}")
# if position == 13:
#     row3 = ["X", "⬜", "⬜"]
#     print(f"{row1}\n{row2}\n{row3}")
#
# if position == 21:
#     row1 = ["⬜", "X", "⬜"]
#     print(f"{row1}\n{row2}\n{row3}")
# if position == 22:
#     row2 = ["⬜", "X", "⬜"]
#     print(f"{row1}\n{row2}\n{row3}")
# if position == 23:
#     row3 = ["⬜", "X", "⬜"]
#     print(f"{row1}\n{row2}\n{row3}")
#
# if position == 31:
#     row1 = ["⬜", "⬜", "X"]
#     print(f"{row1}\n{row2}\n{row3}")
# if position == 32:
#     row2 = ["⬜", "⬜", "X"]
#     print(f"{row1}\n{row2}\n{row3}")
# if position == 33:
#     row3 = ["⬜", "⬜", "X"]
#     print(f"{row1}\n{row2}\n{row3}")
#


# row1 = ["⬜", "⬜", "⬜"]
# row2 = ["⬜", "⬜", "⬜"]
# row3 = ["⬜", "⬜", "⬜"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
#
# horizonal = int(position[0])
# vertical = int(position[1])
#
# selected_row = map[vertical - 1]
# selected_row[horizonal - 1] = "X"
# print(f"{row1}\n{row2}\n{row3}")


row1 = ["⯐", "⯐", "⯐"]
row2 = ["⯐", "⯐", "⯐"]
row3 = ["⯐", "⯐", "⯐"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n ")
position = input("Where do you want to put the treasure? ")
horizonal = int(position[0])
vertical = int(position[1])
map[vertical - 1][horizonal - 1] = "⬜"
print(f"{row1}\n{row2}\n{row3}\n ")

