# 20b. Write Python programs to sum the given sequences: 1^2 + 3^2 + 5^2 + ..... + n^2 (Input n)
n=int(input("Enter the value of n : "))   
sum=0
# for i in range(1, n+1):                 # another approach
#     if (i%2!=0):
#         sum=sum+(i**2)
i=1
while(i<=n):
    sum+=(i**2)
    i+=2
print("Sum = ", sum)        

