
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

