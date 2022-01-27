def fib(n):
    a,b=0,1
    if n==0:
        b=0
    else:    
        print(0)
        while n>1:
            a,b,=b,a+b
            print(b)
            n-=1
        return b 
n=int(input("Enter the numbers : "))
fib(n)    