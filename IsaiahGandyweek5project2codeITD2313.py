a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))
print("")
if ((a*a == b*b + c*c) or (a*a + b*b == c*c) or (a*a + c*c == b*b )):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
