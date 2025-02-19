# CALCULATOR APP
#A simple calculator with basic arithmetic operations.
# It Prompts the user to input two numbers and an operation choice.
# It Performs the calculation and display the result.

#Declaring function
def calculator (num1,num2,operation):
    if operation == '+' :
        return num1 + num2
    elif operation == '-' :
        return num1 - num2 
    elif operation == '*' :
        return num1 * num2
    elif  operation == '/' :
        if operation != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero"
    else:
        print("Error: The operation is null")

#program starts running
print("Welcome to Calculator App")
print("**********_ _ _ _ _ _ _***********")

# getting inputs from the user and display of available resources
num1 = float(input("Please Enter Num 1: "))
num2 = float(input("Please Enter Num 2: "))
print("\nAvailable operations:")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")

#calculate the results,display  and terminate execution
operation = input("Enter the operation:")
result = calculator(num1, num2, operation)
print("\nResult:","",result)
print("\nProgram succesfully executed")