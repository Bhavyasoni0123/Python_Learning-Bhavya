print('hello world')
name = "Bhavya Soni"
age = 17
city = "kanpur"
print('my name is :', name)
print('my age is :', age)
print('i belongs to the city of :', city)
a = None
old = True
print(type(a))
print(type(old))
# keywords in python means reserved words. note we cannot put a identifier name as a keyword.
# python is a case sensitive.
a = int(input('enter a number:'))
b = int(input('enter a number:'))
print(a + b)
# comments in python
# comments are preformed by using # for single line and '''_''' for multi line comments.
# TYPE CONVERSION 
a = 20
b = 25.5
print(a + b)
# TYPE CASTING 
a = int('20')
b = 32.56
print(a + b) 
# PRACTICE QUESTIONS - 
# 1 -
a = int(input('enter a number:'))
b = int(input('enter a number:'))
sum = a + b
print(sum)
# 2 - 
side = int(input('enter the side of the square:'))
operation = input('enter the operation you want to preform:')
perimeter = 4 * side
area = side * side
if operation == 'perimeter':
    print('perimeter of the square:', perimeter)
elif operation == 'area':
    print('area of the square:', area)
else:
    print('invalid operation')
# 3 -
a = float(input('enter a number:'))
b = float(input('enter a number:'))
avg_value = (a + b) / 2 
print(avg_value)   

