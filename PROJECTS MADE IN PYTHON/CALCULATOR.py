A = int(input('enter your number A: '))
B = int(input('enter your number B: '))
operation = input('+, -, *, /, %: ')
if operation == '+':
    print(A + B)
elif operation == '-':
    print(A - B)
elif operation == '*':
    print(A * B)
elif operation == '/':
    print(A / B)
elif operation =='%':
    print(A % B)
else:
    print('invalid operation')