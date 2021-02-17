print("Operation options:")
print("1.Basic Calculator, 2.Trigonometry Calculator")
operation=input("Select option (1,2,3,4): ")

if operation not in("1","2"):
    print("Invalid Input")
else:
    if operation=="1":
        import basic_calc
    elif operation=="2":
        import trigo_calc