# 6. Write a short program to check whether the square root of a number is prime or not.
import math
num=int(input("Enter a number : "))
Sq_Rt=math.sqrt(num)
count=0
for i in range(1,int(Sq_Rt+1)):
    if (Sq_Rt%i==0):
        count+=1
if (count==2):
    print("Square root = ",Sq_Rt , "is prime")
else:
    print("Square root = ",Sq_Rt , "is not prime")
            
