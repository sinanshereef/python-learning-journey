
import os

logo='''
 ___________________
|  _________________  |
| | 7 | 8 | 9 | / | |
| |___|___|___|___| |
| | 4 | 5 | 6 | * | |
| |___|___|___|___| |
| | 1 | 2 | 3 | - | |
| |___|___|___|___| |
| | 0 | . | = | + | |
| |___|___|___|___| |
|___________________|

'''
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def add(num1,num2):
    res=num1+num2
    return res
def sub(num1,num2):
    res=num1-num2
    return res
def mul(num1,num2):
    res=num1*num2
    return res
def div(num1,num2):
    res=num1/num2
    return res

operations={
    '+':add,
    '-':sub,
    '*':mul,
    '/':div
}

def calculator():
    print(logo)
    num1=int(input('Enter the 1st Number: '))
    for i in operations:
        print(i)
    should_continue=True

    while should_continue:
        symbol=input('Pick an Operation: ')
        num2=int(input('Enter the 2nd Number: '))
        calculation=operations[symbol]
        answer=calculation(num1,num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        if input(f'if you want to continue with {answer}then type Y or N to start a new Calculation:')=='Y':
            num1=answer
        else:
            should_continue=False
            clear_screen()
            calculator()
calculator()
