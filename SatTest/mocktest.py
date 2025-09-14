'''
1) 
--> python is a high level and interpreted language.
--> python is a also a programming language .
--> python is based on oops concepts.
--> it is a dynamically typed language.
--> which makes it easy to learn and use.
-->  less code is required to perform python task.
'''
'2)'
name= "Welcome to Python Programming"
print(name)
'''
3)
conversion : converting one data type to another data type.
implicit type conversion can be done by interpreter,
example:'''
a=10
b=3
print(a/b)
'''whereas explicit type conversion is done by user.'''
a=10
print(a)
print(type(a))
a=float(a)
print(type(a))
'''
4) a)'''
x=25
print(hex(x))
print(bin(x))
print(oct(x))
'''b)'''
str="1234"
print(type(str))
str=int(str)
print(type(str))
print(str)

'''6)'''
x=int(input('enter a valid numbers:'))
if x%3==0 and x%5==0 and x%10!=0:
    print(x,'divisible by 3 and 5')

'''
7)'''
num=int(input('enter a number:'))
if num%400==0:
    print(num,'is a leap year')
elif num%100!=0 and num%4==0:
    print(num,'is a leap year')
else:
    print(num,'is not a leap year')


'''8)'''
x=499
y=20
z=30
if x>y and x>z:
    print(x ,'is largest number')
elif y>z and y>x:
    print(y, 'is largest number')
else :
    print(z , 'is a largest number')


'''9)'''
marks=int(input('enter your marks:'))
if marks>=90:
    print('Excellent')
elif marks>=75:
    print('Good')
elif marks>=50:
    print('Average')
else:
    print('Fail')

'''10)'''
s=int(input("enter a number:"))
num=1
while num<=10:
    print(s, '*', num, '=',s*num)
    num+=1

