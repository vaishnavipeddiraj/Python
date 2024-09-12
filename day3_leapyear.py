year = int(input('what is the year you want to check?' ))

if year % 4==0:
    if year %100 ==0:
        if year %400==0:
            print(f"the year {year} is leap year")
        else:
            print("its not a leap year")
    else:
        print(f"the year {year} is leap year")
else:
    print("its not a leap year")


#this is much better to understand
year = int(input('What is the year you want to check? '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")