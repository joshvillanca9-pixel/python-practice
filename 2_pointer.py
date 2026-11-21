def add(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
         return 0
    else:
        return a/b


while True:
    print("1. add")
    print("2. minus")
    print("3. multiply")
    print("4. divide")


    picknumber = int(input("chooseNumber: "))

    if picknumber == 1:
        num1 = float(input("Enter num 1:"))
        num2 = float(input("Enter num 2:"))
        print(f"{num1} + {num2} ={add(num1,num2)}")

    elif picknumber == 2:
        num1 = float(input("Enter num 1:"))
        num2 = float(input("Enter num 2:"))
        print(f"{num1} + {num2} ={minus(num1,num2)}")

    elif picknumber == 3:
        num1 = float(input("Enter num 1:"))
        num2 = float(input("Enter num 2:"))
        print(f"{num1} + {num2} ={multiply(num1,num2)}")

    elif picknumber == 4:
        num1 = float(input("Enter num 1:"))
        num2 = float(input("Enter num 2:"))
        print(f"{num1} + {num2} ={divide(num1, num2)}")

    else:
        print("error")





