#PROGRAME 1
name = input('enter your name:' )
age = input('enter your age:')
city = input('enter the name of your city:')
print('My name is ',name)
print('My age is ',age)
print('I belongs to the city of ',city)
#PROGRAME 2 
num_1 = int(input('enter a number:'))
num_2 = int(input('enter a number:'))
operation = input('select the operation you want to preform:')
if operation == '+':
    print(num_1 + num_2)
elif operation == '-':
    print(num_1 - num_2)
elif operation == '*':
    print(num_1 * num_2)
elif operation == '/':
    print(num_1 / num_2)
elif operation == '//':
    print(num_1 // num_2)
elif operation == '%':
    print(num_1 % num_2)
else:
    print('INVALID OPERATION')
#PROGRAME 3
a = int(input('enter a number:'))
if a / 2 == 0:
    print('number is even')
else:
    print('number is odd')
#PROGRAMME 4
a = int(input('enter a number:'))
if a == 0:
    print('zero')
elif a < 0:
    print('negative')
else:
    print('positive')
#PROGRAMME 5
a = int(input('enter a number a:'))
b = int(input('enter a number b:'))
c = int(input('enter a number c:'))
if a > b and a > c:
    print('a is the largest')
elif b > a and b > c:
    print('b is the largest')
else:
    print('c is the largest') 
#PROGRAMME 6
number1 = int(input('enter number1:'))
number2 = int(input('enter number2:'))
operation = input('operation:')
if operation == '+':
    print(number1 + number2)
elif operation == '-':
    print(number1 - number2)
elif operation == '*':
    print(number1 * number2)
elif operation == '/':
    print(number1 / number2)
else:
    print('INVALID OPERATION')
#PROGRAMME 7
a = int(input('enter a number:'))
for i in range(1 , 11):
    print(a * i)
#PROGRAMME 8
user = input('enter your first name:')
print(len(user))
#PROGRAMME 9
str1 = input('enter a string:')
print(str1.count('$'))
# PROGRAMME 10
str_1 = input('enter a string:')
ch = 'aeiou'
count = 0
for i in str_1:
    if i in ch:
        count += 1
print(count)



