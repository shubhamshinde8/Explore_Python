
n=int(input("Enter a Number "))
a=0

for i in range(2,n):
    if(n%i==0):
        a=1

if(a>0):
    print("Not Prime")
else:
    print("Prime")
