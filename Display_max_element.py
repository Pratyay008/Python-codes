# 3.write a program to input two lists and display the maximum element from the elements of both the lists combined along with the index in its list.
list1=eval(input("Enter 1st list elements : "))
list2=eval(input("Enter 2nd list elements : "))
max1=max(list1)
max2=max(list2)
if(max1>max2):
    print("The number is : ", max1, " at index:", list1.index(max1),"in list 1" )
else:    
    print("The number is : ", max2, " at index:", list2.index(max2), "in list 2" )