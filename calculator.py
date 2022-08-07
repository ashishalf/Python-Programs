def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def squa(a):
    return a*a
print('1. Add , 2. Sub, 3. Mul, 4. Div, 5. Squ')
while True:
    c =input('enter your choice : ')
    if c in '1':
        a=int(input('enter first number : '))
        b=int(input('enter second number : '))
        print("Addition : "+str(add(a,b)))
    elif c in '2':
        a=int(input('enter first number : '))
        b=int(input('enter second number : '))
        print("Subtraction : "+str(sub(a,b)))
    elif c in '3':
        a=int(input('enter first number : '))
        b=int(input('enter second number : '))
        print("Multiplication : "+str(mul(a,b)))
    elif c in '4':
        a=int(input('enter first number : '))
        b=int(input('enter second number : '))
        print("Division : "+str(div(a,b)))
    else:
        a=int(input('enter a number : '))
        print("Squar : "+str(squa(a)))