def calc(operator, x, y):
    operators = {'+' : add, '-' : sub, '*' : mult, '/' : div} #I used here dictionary instead of if/elif/else statements
    action = operators.get(operator)
    if action:
        return action(x,y) #depending on given operator executes add, sub, mult, div
    return None

def add(x,y):       #addition
    return x + y

def sub(x,y):       #subtraction
    return x - y

def mult(x,y):      #multiplication
    return x * y

def div(x,y):       #division
    return x / y


def main():
    operator = input('type in operator: ')
    x = float(input('type in first number: '))
    y = float(input('type in second number: '))

    outcome = calc(operator, x, y)
    print(outcome)

if __name__ == '__main__':
    main()
