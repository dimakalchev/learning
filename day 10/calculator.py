logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiple(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {"+": add,
                "-": substract,
                "*": multiple,
                "/": divide,
}

num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)
n = False
while n is False:
    operation_symbol = input("Pick an operation: ")
    num2 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer1 = calculation_function(n1=num1, n2=num2)
    print(f"{num1} {operation_symbol} {num2} = {answer1}\n ")
    cont = input(f"Type 'y' to continue calculating with {answer1}, or type 'n' to exit.: ")

    if cont == "y":
        operation_symbol = input("Pick another operation: ")
        num3 = int(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer2 = calculation_function(n1=answer1, n2=num3)
        print(f"{answer1} {operation_symbol} {num3} = {answer2}")
        cont = input("Type 'y' to continue calculating with {answer1}, or type 'n' to exit.: ")
        num1 = answer2
    else:
        n = True






