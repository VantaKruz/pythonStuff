num=int(input("Enter a number: "))

print("Reverse number: ", end='')
while (num!=0):
    temp=num%10
    print(int(temp), end='')
    num=num//10