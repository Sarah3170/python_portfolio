#Calculator
#Create a progarm that prompts users to enter two numbers, an operator, and prints the result of the operation

#Init
#Function
def main():
    print("Welcome to the Simple Calculator!")

    num1 = int( input("Please enter your first number: ") )
    num2 = int( input("Please enter your second number: ") )
    operator = input("Please enter your operator(+,-,*,/): ")

    #Perform Operation
    if operator == "+":
        print( calc_sum(num1, num2) )
    if operator == "-":
        print( calc_sub(num1, num2) )
    if operator == "/":
        print( calc_div(num1, num2) )
    if operator == "*":
        print( calc_mult(num1, num2) )

def calc_sum(x,y):
    return x + y
def calc_sub(x,y):
    return x - y
def calc_div(x,y):
    return x / y
def calc_mult(x,y):
    return x * y

#Main
main()

