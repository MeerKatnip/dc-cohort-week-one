first_number = float(input('What is your first number?'))
operand = input('What is your operand? (+, -, *, /)')
second_number = float(input('What is your second number?'))

if operand == '+':
    print(first_number + second_number)
elif operand == '-':
    print(first_number - second_number)
elif operand == '*':
    print(first_number * second_number)
elif operand == '/':    
    print(first_number / second_number)
else:
    print("Need a valid operand input")