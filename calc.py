def add(n1,n2):    #functions for operations
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    if n2!=0:
        return n1 / n2
    else:
        return "error: division by zero"  #error handling inn divison

choice=['+','-','*','/',]

n1=float(input("enter number 1:"))  #taking inputs
n2=float(input("enter number 2:"))
operation=(input("Select operation."))
if operation in choice:
   if operation == "+":
      print(add(n1,n2))
   elif operation == "-":
      print(subtract(n1,n2))
   elif operation=="*":
      print(multiply(n1,n2))
   elif operation=="/":
      print(divide(n1,n2))
else:
    print("Invalid input")   #error handling for invalid operation
    
    
    

    
    
    