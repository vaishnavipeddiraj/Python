print("Thank you for choosing python pizza Deliveries!!!")
size = input("what is the size of pizza do you want? S, M, L").lower()
add_pepperoni = input("do you want pepperoni? Y or N").lower()
extra_cheese = input("do you want extra cheese? Y or N").lower()

bill=0
if size =="s":
    bill+=15
elif size =="m":
    bill+=20
else:
    bill+=25

if add_pepperoni =="y":
    if size =="s":
        bill+=2
    else:
        bill+=3

if extra_cheese =="y":
    bill+=1


print(f"your final bill is {bill}")


