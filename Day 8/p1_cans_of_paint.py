# def greet():
#     print("Hello")
#     print("How do u do?")
#     print("Isn't the weather nice today?")
#
# greet()
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do u do {name}?")
# greet_with_name("Bobby")
import math

# def greet_with(name, location):
# #     print(f"Hello, {name}")
# #     print(f"What is it like in {location} ")
# # greet_with(name="America", location= "Dima")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
import math

def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {number_of_cans} cans of paint. ")


paint_calc(height=test_h, width=test_w, cover=coverage)

