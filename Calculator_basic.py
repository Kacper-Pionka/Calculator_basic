def calc(operator, x, y):
    operators = {'+' : add, '-' : sub, '*' : mult, '/' : div}
    action = operators.get(operator)
    if action:
        return action(x,y)
    return None

def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mult(x,y):
    return x * y
def div(x,y):
    return x / y

def calculator():
    operator = input('type in operator: ')
    x = float(input('type in first number: '))
    y = float(input('type in second number: '))

    outcome = calc(operator, x, y)
    print(outcome)

calculator()
