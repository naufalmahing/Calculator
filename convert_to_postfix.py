
priority = {
    '+': 2,
    '-': 2,
    '*': 3,
    '/': 3
}

def higherorequalpriority(stack, char):
    if stack and char not in '()':
        if char and stack in '+-*/':
            if priority.get(stack) >= priority.get(char):
                return True
            else:
                return False

def peek(array):
    if len(array) != 0:
        return array[len(array)-1]

def isempty(array):
    if len(array) == 0:
        return True
    return False

def isleftparenthesis(c):
    if c == '(':
        return True
    return False

def isrightparenthesis(c):
    if c == ')':
        return True
    return False

def isoperand(s):
    for c in s:
        if c in "+-*/()":
            return True
    return False

def split(s):
    arr = []
    temp = ''
    s += ' '
    for i in range(len(s)):
        if isoperand(s[i]):
            if temp != '':
                arr.append(temp)
            arr.append(s[i])
            temp = ''
        elif s[i].isdigit():
            temp += s[i]
        elif s[i] == ' ':
            if temp != '':
                arr.append(temp)
    return arr

def infixtopostfix_splitted(s):
    s.append(')')
    stack = ['(']
    # postfix = ''
    postfix = []

    for c in s:
        if isoperand(c):
            if isrightparenthesis(c):
                while True:
                    if isleftparenthesis(peek(stack)) and len(stack) != 1:
                        stack.pop()
                    elif len(stack) == 1:
                        break
                    else:
                        print("jalan " + peek(stack))
                        postfix += stack.pop()
            elif higherorequalpriority(peek(stack), c):
                postfix.append(stack.pop())
                stack.append(c)
            elif not higherorequalpriority(peek(stack), c):
                stack.append(c)
        else:
            postfix.append(c)

    return postfix

def infixtopostfix(s):
    s += ')'
    stack = ['(']
    postfix = ''

    for c in s:
        if isoperand(c):
            if isrightparenthesis(c):
                while True:
                    if isleftparenthesis(peek(stack)) and len(stack) != 1:
                        stack.pop()
                    elif len(stack) == 1:
                        break
                    else:
                        print("jalan " + peek(stack))
                        postfix += stack.pop()
            elif higherorequalpriority(peek(stack), c):
                print("pop " + peek(stack))
                postfix += stack.pop()
                stack.append(c)
                print("tambah lebih tinggi " + c)
            elif not higherorequalpriority(peek(stack), c):
                stack.append(c)
                print("tambah lebih rendah " + c)
        else:
            postfix += c
        print(c)
    print(stack)
    return postfix
