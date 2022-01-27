# 1. A store charges ₹120 per item if you buy less than 10 items. If you buy between 10 and 99 items, the cost is ₹100 per item. If you buy 100 or more items, the cost is ₹70 per item. Write a program that asks the user how many items they are buying and prints the total cost.
item=int(input("Enter the number of items : "))
if (item<10):
    print("The total cost is : ", item*120)
elif (10 <=item <=99):
    print("The total cost is : ", item*100)
else:
    print("The total cost is : ", item*70)
        





# another approach of doing this example        
n=int(input("Enter the number of items : "))
cost=0
if(n<10):
    cost=n*120
elif (n<100):
    cost=n*100
else:
    cost=n*70
print("Total Cost is = ",cost)    