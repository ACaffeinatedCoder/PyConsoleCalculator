# ACaffeinatedCoder's Basic Console Python Calculator
# Structure:
#   user input first digit
#   user input operation
#   user input second digit
#   catch type error exception
#   display answer
#   loop

while True:
    try:
        first_digit = float(input("Enter first number: "))
        operation = input("Enter operation: ")
        second_digit = float(input("Enter second number: "))
        if operation == '+':
            answer = first_digit + second_digit
            print("Answer: " + str(answer))
        elif operation == '-':
            answer = first_digit - second_digit
            print("Answer: " + str(answer))
        elif operation == '*':
            answer = first_digit * second_digit
            print("Answer: " + str(answer))
        elif operation == '/':
            answer = first_digit / second_digit
            answer2 = first_digit % second_digit
            print("Answer: " + str(answer) + " Remainder: " + str(answer2))
        elif operation == '%':
            answer = first_digit % second_digit
            print("Answer: " + str(answer))
        else:
            print("You made an invalid input for the operation. Please try again.")
    except ZeroDivisionError:
        print("You tried to divide by zero. It is mathematically impossible.")
    except ValueError:
        print("You made an invalid input. Please try again.")
