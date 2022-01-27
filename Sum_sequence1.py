# 2. Write Python programs to sum the given sequences: 2/9 - 5/13 + 8/17 ...... (print 7 terms)
d, a, b = 1, 2, 9
sum = 0
for i in range(7):
    temp=a/b
    sum= sum+(temp*d)
    a+=3
    b+=4
    d*=-1
print("Sum = ",sum) 




# i,d, a, b = 1, 1, 2, 9                # another rule
# sum = 0
# while(i<=7):
#     s = a/b
#     sum = sum+ s*d
#     a+=3
#     b+=4
#     i+=1
#     d=d*-1
# print("Sum = ",sum)    
