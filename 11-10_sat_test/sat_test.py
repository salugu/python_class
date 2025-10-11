
# mock test
'''1)
mutable: in which value  can be changed 
immutable: once we create an object then it cannot be changed
mutable: list
immutable:tuple
'''

'''2)
= operator: is an assignment operator to assign the values
== operator:is a comparison operator to compare the values,if both values are true then it returns true if not false
'''

'''3)
'''
x = 10
y = 10
print(x is y, x == y)
#_output true true

'''5)'''
s = "pythonprogramming"
print(s[::-1][3:8])
#_output mmarg

'''6)'''
x = [1, 2, 3]
y = x
y.append(4)
print(x, y)
#_output [1, 2, 3, 4] [1, 2, 3, 4]

'''7)'''
t = (1, 2, 3, 2, 1)
print(t.index(2), t.count(1))
#_output 1 2

'''8)'''
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b, a | b, a - b)
#_output {3} {1, 2, 3, 4, 5} {1, 2}

'''9)'''
s2="saicharan"
x=0
y=0
for i in s2:
    if i in 'aeiou':
        x+=1
    else:
        y+=1
print("the vowels are " ,x)
print("the consonents are ",y)

'''10)
'''
num=12
if num > 1:
    for i in range(2, int(num*0.5) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

'''11)'''
def remove_duplicates(s):
    result = []
    for item in s:
        if item not in result:
            result.append(item)
    return result
n= [1,3,2,13,22,123,21,2,1,1]
print(remove_duplicates(n))

'''13)'''
def func(a, b, *args, **kwargs):
    print("Positional argument:", a)
    print("Default argument:", b)
    print("Variable length arguments:", args)
    print("Keyword arguments:", kwargs)

func(1,2,3,4,5,key1='value1', key2='value2')

'''14)'''
def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
    else:
        return "Invalid operation"
print(calculate(10, 5, '+'))
print(calculate(10, 5, '-'))
print(calculate(10, 5, '*'))    
print(calculate(10, 5, '/'))
'''output 
15
5 
50
2
'''


'''15)'''
for i in range (1,6):
    for j in range(1,i+1):

        print(j,end=' ')
    print()
'''output
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

'''



