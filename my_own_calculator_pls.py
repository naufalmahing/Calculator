import convert_to_postfix as ctp

def hitungpostfix(array):
    array.append(')')
    stack = []
    for element in array:
        if ctp.isrightparenthesis(element):
            break
        if ctp.isoperand(element):
            if element == '+':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.insert(len(stack), int(op1) + int(op2))
            elif element == '-':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.insert(len(stack), int(op1) - int(op2))
            elif element == '*':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.insert(len(stack), int(op1) * int(op2))
            elif element == '/':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.insert(len(stack), float(op1) / float(op2))
        elif element.isdigit():
            stack.append(element)
    return stack[0]

formula = ''
run = True
while True:
    if run:
        formula = (input('Masukkan formula yang ingin dihitung: \n'))
        print(hitungpostfix(ctp.infixtopostfix_splitted(ctp.split(formula))))
    exit = input('Masukkan y/n untuk lanjut/keluar: ')
    if str.lower(exit) == 'n':
        break
    elif str.lower(exit) != 'y':
        run = False
    elif str.lower(exit) == 'y':
        run = True     


