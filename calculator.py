def add(a,b):
    return(a+b)
   

def subtract(a,b):
    return(a-b)
  

def multiply(a,b):
    return(a*b)
   

def divide(a,b):
    if b ==0:
        return "Giving an error!divided by zero"
    return(a/b)

print("1 - Add")
print("2 - Subtract")
print("3 - multiply")
print("4 - divide")
option = int(input("choose an option: "))

if option in [1,2,3,4,]:

    num1 = float(input("Enter your first number: "))  
  
    num2 = float(input("Enter your second number: "))  

    if (option ==1):
       result = add(num1, num2)

    elif(option ==2):
        result = subtract(num1, num2)

    elif(option ==3):
        result = multiply(num1, num2)

    elif(option ==4):
        result = divide(num1, num2)

    print("The result of the opreation is {}" .format(result))

else:
    print("Invalid opertaion entered")
