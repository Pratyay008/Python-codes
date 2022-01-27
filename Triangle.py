# 3. Write a program to input 3 sides of a triangle and print whether it is an equilateral, scalene or isosceles triangle.
a=int(input("Enter first side :"))
b=int(input("Enter second side :"))
c=int(input("Enter third side :"))
if(a==b==c):
    print("This is equilateral triangle")
elif(a==b or b==c or a==c):
    print("This is isosceles triangle")
else:
    print("This is scalene triangle")
    
    