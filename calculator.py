print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
option = int(input("choose an option: "))

if option in [1,2,3,4,]:

    num1 = float(input("Enter your first number: "))  
  
    num2 = float(input("Enter your second number: "))  

    if (option ==1):
        result = num1 +num2


    elif(option ==2):
        result = num1 - num2

    elif(option ==3):
        result = num1*num2

    elif(option ==4):
        result = num1/num2

    print("The result of the opreation is {}" .format(result))

else:
    print("Invalid opertaion entered")