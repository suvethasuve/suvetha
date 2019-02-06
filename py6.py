number1 = float(input())
number2 = float(input())
number3 = float(input())
 
if (number1 > number2) and (number1 > number3):
   largest = number1
elif (number2 > number1) and (number2 > number3):
   largest = number2
else:
   largest = number3
 
print("The largest number is",largest)
