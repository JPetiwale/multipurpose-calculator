import math
from tkinter import *

#defination

#Simple Interest
def I_total(P,r,t):
    return (p*r*t)/100

def P_total(i,r,t):
    return (i*100)/(r*t)

def R_total(p,i,t):
    return (i*100)/(p*t)

def T_total(i,r,p):
    return (i*100)/(p*r)

#Permutation & Combination
def permutation(n,r):
    return math.perm(n,r)

def combination(n,r):
    return math.comb(n,r)

def print_detail():
    print("n=set size; The total number of items in the sample")
    print("r=set subsize; The total number of items to be selected from the sample")

#Program

def main():
    #Main Start
    while True:
        #print("\n" * 50)  --> this to clear screen upto 50 lines
        print("""
        Operation options: 
        1.Basic Calculator
        2.Trigonometry Calculator
        3.Simple Interest Calculation
        4.Permutation And Combination
        5.Actual Calculator
        Enter 0 to exit
        """)
        operation=input("Select option (0/1/2/3/4/5): ")

        #Main inavlid if else
        if operation not in("0","1","2","3","4","5"):
            print("Invalid Input")
        else:
        #Basic Calculator    
            if operation=="1":
                print("Basic Calculator")
                basic_calculator()
        #Trigonometry        
            elif operation=="2":
                print("Trignometry Calculator")
                trigonometry_calculator()
        #Simple Interest
            elif operation=="3":
                print("Simple Interest Calculation")
                simple_interest_calculator()
        #Permutation And Combination
            elif operation=="4":
                print("Permutation And Combination")
                PnC()
            #Acutal Calculator
            elif operation=="5":
                print("Actual Calculator")
                actual_calculator()
            elif operation=="0":
                print("Thank you for using JP Multipurpose Calculator")
                return False
#main ended

def basic_calculator():
    print("""
    Operations option:
            1.Addition                 2.Substract
            3.Multiplication           4.Division
    """)
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

def trigonometry_calculator():
    print("""
    Operations option:
            1.sin       2.cos
            3.tan       4.cot
            5.sec       6.cosec
    """)
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

def simple_interest_calculator():
    print("""
    Operations option: 
        1. Interest Amount
        2. Principle Amount
        3. Rate of Interest per year in percent
        4. Time Period in Year
    """)
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

def actual_calculator():
    expression=""

    def press(num):
        global expression
        expression=expression + str(num)
        equation.set(expression)

    def equalpress():
        try:
            global expression
            total=str(eval(expression))
            equation.set(total)
            expression=""
        except:
            equation.set("error")
            expression=""

    def clear():
        global expression
        expression=""
        equation.set("")

    if __name__=="__main__":
        gui=Tk()
        gui.configure(background="Grey")
        gui.title("Calculator")
        gui.geometry("500x300")
        
        equation=StringVar()
        expression_field=Entry(gui,textvariable=equation)
        expression_field.grid(columnspan=4, ipadx=70)

        button1=Button(gui,text="1",fg='black',bg='white',command=lambda: press(1),height=2,width=14)
        button1.grid(row=2,column=0)
        button2=Button(gui,text="2",fg='black',bg='white',command=lambda: press(2),height=2,width=14)
        button2.grid(row=2,column=1)
        button3=Button(gui,text="3",fg='black',bg='white',command=lambda: press(3),height=2,width=14)
        button3.grid(row=2,column=2)
        button4=Button(gui,text="4",fg='black',bg='white',command=lambda: press(4),height=2,width=14)
        button4.grid(row=3,column=0)
        button5=Button(gui,text="5",fg='black',bg='white',command=lambda: press(5),height=2,width=14)
        button5.grid(row=3,column=1)
        button6=Button(gui,text="6",fg='black',bg='white',command=lambda: press(6),height=2,width=14)
        button6.grid(row=3,column=2)
        button7=Button(gui,text="7",fg='black',bg='white',command=lambda: press(7),height=2,width=14)
        button7.grid(row=4,column=0)
        button8=Button(gui,text="8",fg='black',bg='white',command=lambda: press(8),height=2,width=14)
        button8.grid(row=4,column=1)
        button9=Button(gui,text="9",fg='black',bg='white',command=lambda: press(9),height=2,width=14)
        button9.grid(row=4,column=2)
        button0=Button(gui,text="0",fg='black',bg='white',command=lambda: press(0),height=2,width=14)
        button0.grid(row=5,column=0)

        plus=Button(gui,text="+",fg='black',bg='white',command=lambda: press("+"),height=2,width=14)
        plus.grid(row=2,column=3)

        minus=Button(gui,text="-",fg='black',bg='white',command=lambda: press("-"),height=2,width=14)
        minus.grid(row=3,column=3)

        multiply=Button(gui,text="*",fg='black',bg='white',command=lambda: press("*"),height=2,width=14)
        multiply.grid(row=4,column=3)

        divide=Button(gui,text="/",fg='black',bg='white',command=lambda: press("/"),height=2,width=14)
        divide.grid(row=5,column=3)

        equal=Button(gui,text="=",fg='black',bg='white',command=equalpress,height=2,width=14) 
        equal.grid(row=5, column=2)

        clear=Button(gui,text="clear",fg='black', bg='white',command=clear,height=2,width=14) 
        clear.grid(row=5,column=1)

        Decimal=Button(gui,text='.',fg='black', bg='white',command=lambda: press("."),height=2,width=14) 
        Decimal.grid(row=6,column=0) 

    #gui.resizable(0,0)
    gui.mainloop()
    print("Thank you for using actual Calculator Functions!")

def PnC():
    print("""
    What will you like to do ?
            1.Permutation       2.Combination
    """)
    operator=input("select your operator: ")

    if operator not in ("1","2"):
        print("Invalid Operator")
    else:
        if operator=="1":
            print("P(n,r): where")
            print(print_detail())
            n=int(input("please enter value of n: "))
            r=int(input("please enter value of r: "))
            print("permutation of P(",n,",",r,") is: ", permutation(n,r))
        elif operator=="2":
            print("C(n,r): where")
            print(print_detail())
            n=int(input("please enter value of n: "))
            r=int(input("please enter value of r: "))
            print("Combination of C(",n,",",r,") is: ", combination(n,r))


#Initiate

main()