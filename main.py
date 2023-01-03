# ACaffeinatedCoder's Basic Console Python Calculator
# Structure:
#   user input first digit
#   user input operation
#   user input second digit
#   add loop breaking option
#   catch zerodivision error exception
#   catch value error exception
#   display answer
#   loop

while True:
    try:
        first_digit = float(input("Enter first number: "))
       operation = input("Enter operation (enter ';' to exit): ")
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
        elif operation == ';':
            break
        else:
            print("You made an invalid input for the operation. Please try again.")
    except ZeroDivisionError:
        print("You tried to divide by zero. It is mathematically impossible.")
    except ValueError:
        print("You made an invalid input. You must only input numerical characters for the digits. Please try again.")
