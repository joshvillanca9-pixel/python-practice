from tokenize import Number


class numbrerings:
    def factorial(a):
        start = 1
        for i in range(1,a+1):
            start = start*i
            print(f"{start}")

    def primeNumber(a):
        if a <=1 :
            return False
        for i in range(2,a):
            if a % i ==0:
                return False
        return True

class motor:
    def __init__(self,name, year, model):
        self.name = name
        self.year = year
        self.model = model

    def whatItdoes(self):
        print(f"This is my first motorcyle the name is {self.name} year {self.year}, model is {self.model}")




mathematcas = numbrerings

name = input("NAme of motor? ")
year = int(input("what year? "))
model = input("what model?")

motor1 = motor(name, year , model)
motor1.whatItdoes()


