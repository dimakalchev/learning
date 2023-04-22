# programming_dictionary = {
#   "Bug": "An error in a programm that prevents the programm from ruining as expected",
#   "Function": "A piece of code that you can easily call over and over again",
#   "Loop": "The action of doing something over an over again",
# }

# programming_dictionary["Pupalupa"] = "Channel on Youtube"
# print(programming_dictionary)

# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

students_score = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

students_grade = {}
for key in students_score:
  if students_score[key] >= 91 and students_score[key] <= 100:
    students_grade[key] = "Outstanding"
    print(f"{key}'s grade is Outstanding")
  elif students_score[key] >= 81 and students_score[key] <=90:
    students_grade[key] = "Exceeds Expectations"
    print(f"{key}'s grade is Exceeds Expectations")
  elif students_score[key] >= 71 and students_score[key] <=80:
    students_grade[key] = "Acceptable"
    print(f"{key}'s grade is Acceptable")
  elif students_score[key] <= 70:
    students_grade[key] = "Fail"
    print(f"{key}'s grade is Fail")
print(students_grade["Harry"])
