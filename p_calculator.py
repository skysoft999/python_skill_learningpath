#Author: Sanu k yadav
import pdb
#pdb.set_trace()


OPERATORS = ['+','-','*', '/' ]

def p_main():
    """The Main FLow"""
    print("Welcome to the functional calculator")
    num1 = p_getNumber()
    operator = p_getOperator()
    num2 = p_getNumber()
    result = p_calculate(num1,operator,num2)
    print("The result is: %s" %result)



def p_getNumber():
    """Input Number"""
    while True:
        s = input("Enter the number \t")
        try:
            return int(s)
        except ValueError:
            print("This is not a number please input a valid number")

def  p_getOperator():
    """input Operator"""
    while True:
            s = input("Enter A Operator ::: eg-: +,-,/,* \t")
            if s in OPERATORS:
                return s
            else:
                print("This is not valid operator")

def p_calculate(num1, operator, num2):
    """Calculator function"""
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2 
    if operator == "*":
       return num1 * num2
    if operator == "/":
        return num1 / num2 
    raise Exception("invalid Operator")

p_main()

