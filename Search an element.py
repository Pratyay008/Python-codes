# 1.write a program to search an element in a given list of numbers.
list=[]
n=int(input("Enter the no of elements : "))
for i in range(n):
    elements=int(input())
    list.append(elements)
ele=int(input("Enter the element to search :"))  
flag=0 
for i in range(n):
    if(ele==list[i]):
        print("Element position is : ", i+1)
        flag+=1 
if(flag==0):
    print("Element not found")               