#!/usr/bin/env python3

#!/usr/bin/env python3

def admin_login(username, password):
    if username == "admin" and password == "12345":
        return "Access granted"
    elif username == "ADMIN" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
   

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 65 and temperature <= 85:
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    

def calculator(operation, num1, num2):
    if operation == "add" or operation == "+":
        return num1 + num2
    elif operation == "subtract" or operation == "-":
        return num1 - num2
    elif operation == "multiply" or operation == "*":
        return num1 * num2
    elif operation == "divide" or operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None


    