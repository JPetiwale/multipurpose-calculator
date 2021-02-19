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