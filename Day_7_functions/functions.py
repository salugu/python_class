
#iseven
def iseven(n):
    if n%2==0:
        print(n,'is an even number')
    else:
        print(n,'is an odd number')
iseven(86)
iseven(23)

#isprime
def isprime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        print(n,' is a prime number ')
    else:
        print(n,"is not a prime number")
isprime(5)
isprime(10)

#factorial

def factorial(a):
    f=1
    for i in range(1,a+1):
        f=f*i
    print(f)

for i in range(1,11):
    factorial(i)

#findfactors
def findfactor(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i,'is the factor of ',num)
findfactor(9)