num1 = float(input("Enter the first value: "))
num2 = float(input("Enter the second value: "))
num3 = float(input("Enter the third value: "))
 if (num1 > num2) and (num1 > num3):
   largest = num1
 elif (num2 > num1) and (num2 > num3):
   largest = num2
 else:
   largest = num3
 print("The largest number between",num1,",",num2,"and",num3,"is",largest)
