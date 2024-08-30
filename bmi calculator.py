print("----------------------------------------------")
print("|                                             |")
print("|                                             |")
print("|        Welcome To BMI calculator            |")
print("|                                             |")
print("|                                             |")
print("|                                             |")
print("----------------------------------------------")







weight=float(input("enter the weight in kg : "))
height=float(input("enter the height in mts : "))
bmi=weight/(height**2)

print("----------------------------------------------")


print("your bmi is ",bmi)
if bmi<=18:
  print("you are underweight.")

elif bmi>18 and bmi<25 :
  print("you are healthy")
  
    
else:
  print("your overweight ")

print("----------------------------------------------")