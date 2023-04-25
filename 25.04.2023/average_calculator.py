def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

def get_input_numbers():
    input_numbers = input("Enter a list of numbers separated by commas: ")
    numbers_list = input_numbers.split(',')
    numbers = []
    for num in numbers_list:
        if num.strip().isdigit():
            numbers.append(int(num.strip()))
    return numbers

def main():
    numbers = get_input_numbers()
    if len(numbers) == 0:
        print("No valid numbers entered.")
        return
    avg = calculate_average(numbers)
    print("The average of the numbers is:", avg)

main()
