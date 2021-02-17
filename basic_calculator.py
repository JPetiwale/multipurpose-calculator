print("Operations option: ")
print("1. Add, 2. Substract, 3. Multiplication, 4. Division")
operator=input("Please select input option: ")

if operator in("1","2","3","4"):
    num1=int(input("Please enter first number: "))
    num2=int(input("Please enter Second number: "))
else:
     print("Invalid Operator")

if operator=="1":
    print(num1,"+",num2,"=",num1+num2)

elif operator=="2":
    print(num1,"-",num2,"=",num1-num2)

elif operator=="3":
    print(num1,"*",num2,"=",num1*num2)

elif operator=="4":
    print(num1,"/",num2,"=",num1/num2)