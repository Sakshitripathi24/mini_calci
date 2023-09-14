#mini calculator

Num1 = int(input("Enter first number: "))
Num2 = int(input("Enter second number: "))

Choice = int(input("enter your choice from 1-4: "))
print("press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division")

if (Choice == 1):
    print("the addition of given number", Num1 + Num2)
    
elif (Choice == 2):
    print("the subtraction of given number", Num1 - Num2)
    
elif (Choice == 3):
    print("the multiplication of given number", Num1 * Num2)      

elif (Choice == 4):
    print("the division of given number", Num1 / Num2)  
    
else:
    print("invalid input")