print("Welcome to Calculator")

first_number: int = int(input("Enter First number: "))
second_number: int = int(input("Enter Second number: "))

def sum(first_number, second_number):
    """ This function calculates the sum of two numbers """
    return f"Sum = {first_number + second_number}"

def subtraction(first_number, second_number):
    """ This function calculates the subtraction of two numbers """
    if first_number > second_number:
        return first_number - second_number
    else:
        return second_number - first_number

def multiply(first_number, second_number):
    return first_number * second_number

def division(first_number, second_number):
    if first_number > second_number:
        return first_number / second_number
    else:
        return second_number / first_number

sum_result = sum(first_number, second_number)
subtraction_result = subtraction(first_number, second_number)
multiply_result = multiply(first_number, second_number)
division_result = division(first_number, second_number)

print("Sum result:", sum_result)
print("Subtraction result:", subtraction_result)
print("Multiply result:", multiply_result)
print("Division result:", division_result)