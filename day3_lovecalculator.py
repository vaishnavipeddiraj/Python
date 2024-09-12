print("the Love Calculator is calculating your score...")
name1= input("what is your name?").lower()
name2=input("what is their name?").lower()

combined_names = name1+name2
t=combined_names.count("t")
r=combined_names.count("r")
u=combined_names.count("u")
e=combined_names.count("e")
first_digit =t+r+u+e

l=combined_names.count("l")
o=combined_names.count("o")
v=combined_names.count("v")
e=combined_names.count("e")
second_digit= l+o+v+e

score=str(first_digit)+str(second_digit)

print(f"the score is {score}")

