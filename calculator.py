import math
import random

def calculator():

    def options():
        print("select the operation you want to perform:")
        print("write 'add' to perform Addition")
        print("write 'subtract' to perform Subtraction")
        print("write 'multiply' to perform Multiplication")
        print("write 'divide' to perform Division")
        print("write 'sqrt' to perform Square Root")
        print("write 'more' to perform more operations")
        print("write 'quit' to perform Exit")

    options()

    while True:

        user_Input=input("enter the command: ")

        if user_Input=="options":
            pass

        elif user_Input=="more":
            print("write 'power' to perform Power")
            print("write 'log' to perform Logarithm")
            print("write 'cos' to perform Cosine")
            print("write 'sin' to perform Sine")
            print("write 'tan' to perform Tangent")
            print("write 'pi' to get the value of Pi")
            print("write 'random' to get a Random Float between both numbers")
            continue

        elif user_Input=="quit":
            print("exiting the calculator")
            break

        elif user_Input=="add":
          try:
            num1=float(input("enter first number: "))
            num2=float(input("enter second number: "))
            print("the sum is",num1+num2)
          except:
              print("some error occured please try again")

        elif user_Input=="subtract":
          try:
            num1=float(input("enter first number: "))
            num2=float(input("enter second number: "))
            print("the difference is",num1-num2)
          except:
              print("some error occured please try again")

        elif user_Input=="multiply":
            try:
                num1=float(input("enter first number: "))
                num2=float(input("enter second number: "))
                print("the product is",num1*num2)
            except:
                print("some error occured please try again")

        elif user_Input=="divide":
            try:
                num1=float(input("enter first number: "))
                num2=float(input("enter second number: "))
                print("the quotient is",num1/num2)
            except:
                print("some error occured please try again")

        elif user_Input=="sqrt":
            try:
                num=float(input("enter the number: "))
                print("the square root is",math.sqrt(num))
            except:
                print("some error occured please try again")

        elif user_Input=="power":
            try:
                base=float(input("enter the base number: "))
                exponent=float(input("enter the exponent number: "))
                print("the result is",math.pow(base,exponent))
            except:
                print("some error occured please try again")
        elif user_Input=="log":
            try:
                num=float(input("enter the number: "))
                print("the logarithm is",math.log(num))
            except:
                print("some error occured please try again")

        elif user_Input=="random":
            try:
                num1=float(input("enter the first number: "))
                num2=float(input("enter the second number: "))
                print("the random number is",random.uniform(num1,num2))
            except:
                print("some error occured please try again")

        elif user_Input=="cos":
            try:
                num1=float(input("enter the angle: "))
                result=str(math.cos(num1))
                print("the cosine value is",result)
            except:
                print("some error occured please try again")


        elif user_Input=="sin":
            try:
                num1=float(input("enter the angle: "))
                result=str(math.cos(num1))
                print("the sine value is",result)
            except:
                print("some error occured please try again")
        
        elif user_Input=="tan":
            try:
                num1=float(input("enter the angle: "))
                result=str(math.tan(num1))
                print("the tangent value is",result)
            except:
                print("some error occured please try again")

        elif user_Input=="pi":
            print("the value of pi is",math.pi)

        else:
            print("invalid input please try again")


calculator()