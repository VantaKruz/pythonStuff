curr=1
prev=0

num=int(input("Enter fibonacci limit: "))
print("0", end=' ')
for x in range(num):
    next=prev+curr
    prev=curr
    curr=next
    print(next, end=' ')
print("")