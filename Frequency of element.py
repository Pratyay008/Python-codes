# 2.write a program to count the frequency of a given element in a list of numbers.
list=eval(input("Enter list elements : "))
ele=int(input("Enter the element : "))
count=list.count(ele)
print("Frequency is : ",count)   
if(ele not in list):
    print("not found")



# another process 
list=eval(input("Enter list elements : "))
ele=int(input("Enter the element : "))
flag=0
for i in range(len(list)):
    if(ele==list[i]):
        flag+=1
print("Frequency is : ",flag)   
if(flag==0):
    print("not found")
