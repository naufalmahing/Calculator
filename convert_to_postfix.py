
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

# stack = ['-', '+', '*']
# c = '+'
# print(hasLessPriorityOrEqualPriority(c, peek(stack)))

# array = [1, 2, 3, 4]
# # array.clear()
# print(peek(array))

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
    # 20+15*51
    # for i in range(len(s)):
    #     print(s[i] + " ", end="")
    # different code
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

# arr = []
# arr.append("Naufal")
# print(arr)
# arr += "Naufal"
# print(arr)
# print(split('20+(15*51)'))

def infixtopostfix_splitted(s):
    # s += ')'
    # s.split("+-*/()")
    # operator = ''
    # for c in s:
    #     if isoperand(c):
    #         operator += c
    # stack = ['(']
    # postfix = ''

    # if isinstance(s, list):
    #     print("ini list")

    s.append(')')
    stack = ['(']
    # postfix = ''
    postfix = []

    for c in s:
        if isoperand(c):
            if isrightparenthesis(c):
                # while not isleftparenthesis(c) and len(stack) != 1:
                #     postfix += stack.pop()
                while True:
                    if isleftparenthesis(peek(stack)) and len(stack) != 1:
                        stack.pop()
                        # break
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

# print(infixtopostfix_splitted(split('20+10*50')))
# print(infixtopostfix_splitted(split('20+(10*50)')))
# print(infixtopostfix_splitted(split('(20+10)*50')))

# stck = []
# formula = '2*(3+1)'
# for c in formula:
#     if isoperand(c):
#         stck.append(c)
#
# print(stck, end="")

def infixtopostfix(s):
    s += ')'
    stack = ['(']
    postfix = ''

    for c in s:
        if isoperand(c):
            if isrightparenthesis(c):
                # stack.append(c)
                # print("tambah " + c, end="")
                # if isleftparenthesis(peek(stack)):
                #     stack.pop()
                # else:
                while True:
                    if isleftparenthesis(peek(stack)) and len(stack) != 1:
                        stack.pop()
                        # break
                    elif len(stack) == 1:
                        break
                    else:
                        print("jalan " + peek(stack))
                        postfix += stack.pop()
                    # if isleftparenthesis(peek(stack)):
                    #     break

                    # while not isleftparenthesis(peek(stack)) and len(stack) != 1:
                    #     print("jalan " + peek(stack))
                    #     postfix += stack.pop()
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
        # print("1", end="")
        print(c)
    print(stack)
    return postfix

# print(infixtopostfix('2+(1*5)'))
# print(infixtopostfix('2+1*5'))
# print(infixtopostfix('(2+1)*5'))


# s = '3*(x+1)-2/2'
# print(isOperand(s))

# # just testing something, dX
# empty_array = []
# print(empty_array) # error if u use an index
# array = ["me, ", 1, " am ", "pr", 0, " af"]
# # use index in an array
# for i in range(len(array)):
#     print(array[i], end="")
# print("")
# # use elements in an array
# for i in array:
#     print(i, end="")
# # s = input("Input formula: ")