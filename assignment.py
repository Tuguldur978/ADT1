# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Push() and Pop() - move TopOfStack yourself.

# Exercise 1
Stack = [1] * 10
TopOfStack = -1
# Write code here to fill Stack with 10 elements, all -1


def IsEmpty():
    global Stack, TopOfStack
    return TopOfStack
    
def IsFull():
    global Stack, TopOfStack
    return TopOfStack == 9


# Exercise 2
def Push(Item):
    global Stack, TopOfStack
    if IsFull():
        return False
    TopOfStack += 1
    Stack[TopOfStack] = Item
    return True


# Exercise 3
def Pop():
    global Stack, TopOfStack
    if IsEmpty():
        return -1
    item = Stack[TopOfStack]
    TopOfStack -= 1
    return item

# Exercise 4
def Peek():
    global Stack, TopOfStack
    if IsEmpty():
        return -1
    return Stack[TopOfStack]


def Size():
    global Stack, TopOfStack
    return TopOfStack + 1


# Exercise 5
def ReverseWord(Word):
    global Stack, TopOfStack
    TopOfStack = -1
    for char in Word:
        TopOfStack += 1
        Stack[TopOfStack] = char
    reversed_word = ""
    while TopOfStack != -1:
        reversed_word += Stack[TopOfStack]
        TopOfStack -= 1
    return reversed_word
