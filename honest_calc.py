# write your code here
messages = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):",
    "Do you want to continue calculations? (y / n):",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)",
    "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "Last chance! Do you really want to embarrass yourself? (y / n)"
]
operator_list = ["+", "-", "*", "/"]
memory = 0
result = 0
minus = '-'


def is_number(string):
    try:
        int(string)
        return True
    except ValueError:
        try:
            float(string)
            return True
        except ValueError:
            return False


def check(v1, v2, oper):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + messages[6]
        if (v1 == '1' or v2 == '1') and oper == "*":
            msg = msg + messages[7]
        if (v1 == '0' or v2 == '0') and oper != "/":
            msg = msg + messages[8]
        if msg != "":
            msg = messages[9] + msg
        print(msg)


def is_one_digit(v):
    if float(v).is_integer() and -10 < float(v) < 10:
        return True
    return False


while True:
    answer = ''
    equation = input(messages[0])
    operand_list = equation.split(' ')
    x, operator, y = operand_list
    if x == 'M':
        x = str(memory)
    if y == 'M':
        y = str(memory)

    if not is_number(x) or not is_number(y):
        print(messages[1])
        continue
    if operator not in operator_list:
        print(messages[2])
        continue
    check(x, y, operator)
    x, y = float(x), float(y)
    match operator:
        case '+':
            result = x + y
        case '-':
            result = x - y
        case '*':
            result = x * y
        case '/':
            if y == 0:
                print(messages[3])
                continue
            result = x / y
    print(result)
    while answer not in ['y', 'n']:
        answer = input(messages[4]).casefold()
    if answer == 'y':
        if not is_one_digit(str(result)):
            memory = result
        else:
            msg_index = 10
            while msg_index <= 12:
                answer = input(messages[msg_index]).casefold()
                if answer == 'y':
                    msg_index += 1
                    if msg_index == 12:
                        memory = result
                elif answer == 'n':
                    break
    else:
        memory = 0
    answer = ''
    while answer not in ['y', 'n']:
        answer = input(messages[5]).casefold()
    if answer == 'y':
        continue
    elif answer == 'n':
        break
