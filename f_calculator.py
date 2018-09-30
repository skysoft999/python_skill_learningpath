
OPERATORS = ['+','-','*', '/' ]

def f_main():
    """The Main FLow"""
    return f_calculate(f_getNumber(),
            f_getOperator(),
            f_getNumber(),)



def f_calculate(num1,operator,num2):
        return num1 + num2 if operator =='+'\
                else num1 - num2 if operator == '-'\
                else num1 / num2 if operator=='/'\
                else num1 * num2 if operator=='*'\
                else None
                
def f_getNumber():
    return int(input("Enter Number:"))

def f_getOperator():
    return input("Enter an operator:")

print('The result is : %s' %f_main())

