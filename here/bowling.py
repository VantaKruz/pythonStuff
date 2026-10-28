pins=int(input("Enter number of pins: "))
throws=int(input("Enter numner of throws: "))

pin=['|'] * pins
for x in range(throws+1):
    if(x!=0):
        ki=int(input(f"Enter {x} throw start value: "))
        kf=int(input(f"Enter {x} throw end while: "))
        while(ki<=kf):
            pin[ki-1]='.'
            ki+=1

for x in pin:
    print(f"{x} ", end='')
print()