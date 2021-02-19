import math

#defination
def I_total(P,r,t):
    return (p*r*t)/100

def P_total(i,r,t):
    return (i*100)/(r*t)

def R_total(p,i,t):
    return (i*100)/(p*t)

def T_total(i,r,p):
    return (i*100)/(p*r)

#Main start
print("Operation options:")
print("1.Basic Calculator, 2.Trigonometry Calculator, 3.Simple Interest Calculation")
operation=input("Select option (1/2/3): ")

#Main inavlid if else
if operation not in("1","2","3"):
    print("Invalid Input")
else:
#Basic Calculator    
    if operation=="1":
        print("Basic Calculator")
        print("Operations option: ")
        print("1. Add, 2. Substract, 3. Multiplication, 4. Division")
        Basic_operator=input("Please select input option(1/2/3/4) : ")

        if Basic_operator in("1","2","3","4"):
            num1=int(input("Please enter first number: "))
            num2=int(input("Please enter Second number: "))
        else:
            print("Invalid Operator")

        if Basic_operator=="1":
            print(num1,"+",num2,"=",num1+num2)

        elif Basic_operator=="2":
            print(num1,"-",num2,"=",num1-num2)

        elif Basic_operator=="3":
            print(num1,"*",num2,"=",num1*num2)

        elif Basic_operator=="4":
            print(num1,"/",num2,"=",num1/num2)
        
#Trigonometry        
    elif operation=="2":
        print("Trignometry Calculator")
        print("Operations option: ")
        print("1.sin, 2.cos, 3.tan, 4.cot, 5.sec, 6.cosec")
        trigo_operator=input("Please select a option(1/2/3/4/5/6): ")

        if trigo_operator in("1","2","3","4","5","6"):
            degree=int(input("Please enter degree: "))
        else:
            print("Invalid Operator")

        if trigo_operator=="1":
            print("sin of",degree,"is",math.sin(math.radians(degree)))

        elif trigo_operator=="2":
            print("cos of",degree,"is",math.cos(math.radians(degree)))

        elif trigo_operator=="3":
            print("tan of",degree,"is",math.tan(math.radians(degree)))

        elif trigo_operator=="4":
            print("cot of",degree,"is",math.co(math.radians(degree)))

        elif trigo_operator=="5":
            print("sec of",degree,"is",math.sin(math.radians(degree)))

        elif trigo_operator=="6":
            print("cosec of",degree,"is",math.sin(math.radians(degree)))

#Simple Interest
    elif operation=="3":
        print("Simple Interest Calculation")
        print("Operations option: ")
        print("1. Interest Amount")
        print("2. Principle Amount")
        print("3. Rate of Interest per year in percent")
        print("4. Time Period in Year")
        #print("5. Accursed Amount")

        SI_operator=input("Please select input option(1/2/3/4): ")

        if SI_operator not in("1","2","3","4"):
            print("Invalid Operator")

        if SI_operator=="1":
            p=float(input("Please enter princple amount: Rs."))
            r=float(input("Please enter Rate of Interest per year in Percent(%): "))
            t=float(input("Please enter Time Duration in Year: "))
            print("Interest Amount = Rs.",I_total(p,r,t))

        elif SI_operator=="2":
            i=float(input("Please enter interest amount: Rs."))
            r=float(input("Please enter Rate of Interest per year in Percent(%): "))
            t=float(input("Please enter Time Duration in Year: "))
            print("Principle Amount = Rs.",P_total(i,r,t))

        elif SI_operator=="3":
            p=float(input("Please enter princple amount: Rs."))
            i=float(input("Please enter interest amount: Rs."))
            t=float(input("Please enter Time Duration in Year: "))
            print("Rate of Interest = ",R_total(p,i,t),"%")

        elif SI_operator=="4":
            i=float(input("Please enter interest amount: Rs."))
            r=float(input("Please enter Rate of Interest per year in Percent(%): "))
            p=float(input("Please enter princple amount: Rs."))
            print("Time = ",T_total(i,r,p)," Years")

#end