import math

def permultation(n,r):
    return math.perm(n,r)

def combination(n,r):
    return math.comb(n,r)

print("What will you like to do ?")
print("1.Permutation, 2.Combination")
operator=input("select your operator: ")

if operator not in ("1","2"):
    print("Invalid Operator")
else:
    if operator=="1":
        print("P(n,r): where")
        print("n=set size; The total number of items in the sample")
        print("r=set subsize; The total number of items to be selected from the sample")
        n=int(input("please enter value of n: "))
        r=int(input("please enter value of r: "))
        print("permutation of P(",n,",",r,") is: ", permultation(n,r))
    elif operator=="2":
        print("C(n,r): where")
        print("n=set size; The total number of items in the sample")
        print("r=set subsize; The total number of items to be selected from the sample")
        n=int(input("please enter value of n: "))
        r=int(input("please enter value of r: "))
        print("Combination of C(",n,",",r,") is: ", combination(n,r))