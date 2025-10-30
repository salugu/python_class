year=int(input('enter a valid year:'))
while year<=3000:
    if year%400==0:
        print(year,'entered year is leap year')
    elif year%4==0:
        print(year,'entered year is leap year')
    else:
        print(year,'entered year is not a leap year')
    year+=1

