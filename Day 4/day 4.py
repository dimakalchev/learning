# import random
# random_int = random.randint(1, 100)
# print(random_int)

# random_float = random.random()
# print(random_float)

# random_float = random_float * 5
# print(random_float)

# love_score = random.randint(1,100)
# print(f"Your lovescore is {love_score}")

# Heads or tails
# import random

# random_int = random.randint(0, 1)

# if random_int == 0:
#   print("Heads")
# else:
#   print("Tails")

fruits = ["Apple","Ananas", "Pinapple"]
fruits.extend(["Bananas", "Strawberry"])
print(fruits)

village = ["Volnoe"]
village.append("Vinogradovka")
village.extend(["Novoivanovka, Artsyz"])
print(village)
village.insert(1, "Tarutino")
print(village)
village.remove("Volnoe")
print(village)
village.pop(0)
print(village)