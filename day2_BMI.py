height=float(input())
weight=int(input())

bmi=weight/height**2

if bmi <18.5:
	print(f"yourr bmi is {bmi}, you are underweight")

elif bmi <25:
	print(f'your bmi is {bmi}, you are normal')

else:
	print(f"your bmi is {bmi}, you are obese")