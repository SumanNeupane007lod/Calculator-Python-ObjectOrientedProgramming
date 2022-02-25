
class calculator:
    def add(self,a,b):
        return  a +b
    
    def subtraction(self,a,b):
        return a - b
    
    def multiply(self,a,b):
        return a * b

    def division(self,a,b):
        return a / b
    
cal1=calculator()

while True:
    print('''
       Please Choose the Calculation you want to do :
        1:  >>>>ADDITIONAL
        2.  >>>>SUBTRACTION
        3.  >>>>MULTIPLY
        4.  >>>>DIVISION
        5.  >>>>EXIT
    ''')
    ch=int(input("SELECT :\n"))
    if ch in (1,2,3,4,5):
        if (ch ==5):
            break
        a=int(input("Enter First Number:\n"))
        b=int(input("Enter Second Number:\n"))
        if ch ==1:
            print("Additional :",cal1.add(a,b))
        elif ch ==2:
            print("Subtrction :",cal1.subtraction(a,b))

        elif ch ==3:
            print("Multiple :",cal1.multiply(a,b))

        elif ch ==4:
            print("Division",cal1.division(a,b))    
        

    else:
        print("Please enter Digit mention :")

