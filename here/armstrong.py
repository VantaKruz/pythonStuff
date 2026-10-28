import math

num=int(input("Enter a number= "))
n=int(num)
sum=0
while(n!=0):
    r=n%10
    sum+=r**(len(str(num)))
    n//=10
print(sum)
if(sum==num):
    print("Number is armstrong number ")
else:
    print("Number is not armstrong number")