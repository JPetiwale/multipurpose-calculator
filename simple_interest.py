def I_total(P,r,t):
    return (p*r*t)/100

def P_total(i,r,t):
    return (i*100)/(r*t)

def R_total(p,i,t):
    return (i*100)/(p*t)

def T_total(i,r,p):
    return (i*100)/(p*r)

print("Operations option: ")
print("1. Interest Amount")
print("2. Principle Amount")
print("3. Rate of Interest per year in percent")
print("4. Time Period in Year")
#print("5. Accursed Amount")

operator=input("Please select input option: ")

if operator not in("1","2","3","4"):
     print("Invalid Operator")

if operator=="1":
    p=float(input("Please enter princple amount: "))
    r=float(input("Please enter Rate of Interest per year in Percent: "))
    t=float(input("Please enter Time Duration in Year: "))
    print("Interest Amount = ",I_total(p,r,t))

elif operator=="2":
    i=float(input("Please enter interest amount: "))
    r=float(input("Please enter Rate of Interest per year in Percent: "))
    t=float(input("Please enter Time Duration in Year: "))
    print("Principle Amount = ",P_total(i,r,t))

elif operator=="3":
    p=float(input("Please enter princple amount: "))
    i=float(input("Please enter interest amount: "))
    t=float(input("Please enter Time Duration in Year: "))
    print("Rate of Interest = ",R_total(p,i,t),"%")

elif operator=="4":
    i=float(input("Please enter interest amount: "))
    r=float(input("Please enter Rate of Interest per year in Percent: "))
    p=float(input("Please enter princple amount: "))
    print("Time = ",T_total(i,r,p)," Years")