print("Operation options:")
print("1.Basic Calculator, 2.Trigonometry Calculator")
operation=input("Select option (1,2): ")

if operation not in("1","2"):
    print("Invalid Input")
else:
    if operation=="1":
        print("Basic Calculator")
        import basic_calc
    elif operation=="2":
        print("Trignometry Calculator")
        import trigo_calc
    elif operation=="3":
        print("Simple Interest Calculation")
        import simple_interest