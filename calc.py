print("Welcome to Calculator")

first_number: int = int(input("Enter First number: "))
second_number: int = int(input("Enter Second number: "))

def sum(first_number, second_number):
    return first_number + second_number

def subtraction(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

sum_result = sum(first_number, second_number)
subtraction_result = subtraction(first_number, second_number)
multiply_result = multiply(first_number, second_number)

print("Sum result:", sum_result)
print("Subtraction result:", subtraction_result)
print("Multiply result:", multiply_result)