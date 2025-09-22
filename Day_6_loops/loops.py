
i = 0
while i < 5:
    print(i)
    i += 1

# nested loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")        
# for loop
'''fibonacci series'''
a=0
b=1
for i in range(1,100):
    print(a,end=' ')
    c=a+b
    a=b
    b=c

'''prime numbers'''
n=int(input('enter a number'))
for i in range(1,n+1):
    count=0
    for j in range (1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i, 'is a prime number')
    else:
        print(i,'not a prime number ')

'''patterns'''

for i in range (1,6):
    for j in range(1,6):
        if i>=j:
            print('* ',end=' ')
    print()


n=int(input('enter a number'))
for i in range(1,n+1):
    print(" * "*(n-i+1))

n=int(input('enter a number'))
for i in range (1,n+1):
    print('* ' *(n-i))

n=int(input('ENTER A NUMBER :'))
for i in range(1,n):
        print(''*(n-i), end='')
        print('* '*i)
