import math

print("Operations option: ")
print("1.sin, 2.cos, 3.tan, 4.cot, 5.sec, 6.cosec")
trigo_operator=input("Please select a option: ")

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
