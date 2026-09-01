# STRINGS IN PYTHON
str1 = '''this is a string.
We are creating it in python.'''
print(str1)
print(len(str1))
ch = str1[10]
print(ch)
# slicing of string with positive index -
print(str1[0 : 4])
print(str1[0 :])
# slicing of string with negative index - 
print(str1[: -1])
# strings functions - 
print(str1.endswith('python.'))
print(str1.capitalize())
print(str1.find('o'))
print(str1.count('r'))
# CONDITIONAL STATEMENTS IN PYTHON
user_age = int(input('enter your age:'))
if user_age >= 18:
    print('you are eligible to vote and can apply for a driving license.')
else:
    print('you are not eligible to vote and cannot apply for a driving license.')
# PASSWORD STRENGTH CHECKER -
user_password = input('enter your password:')
if len(user_password) < 8:
    print('your password is weak. it should be at least 8 characters long.')
else:
    print('your password is strong.')
# PROGRAMME TO CHECK THE GRADE OF A STUDENT BASED ON MARKS -
student_marks = int(input('enter the marks of the student:'))
if student_marks >= 90:
    print('grade A')
elif student_marks >=80 and student_marks < 90:
    print('grade B')
elif student_marks >= 70 and student_marks < 80:
    print('grade C')
else:
    print('needs improvement.')
# PROGRAMME TO CHECK WHETHER A NUMBER IS EVEN OR ODD -
num1 = int(input('enter a number:'))
if num1 % 2 == 0:
    print('the number is even.')
else:
    print('the number is odd.')

