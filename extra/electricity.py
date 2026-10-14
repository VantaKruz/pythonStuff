units=int(input("Enter units consumed: "))
bill=0
if(units<=100):
    bill=units*5
elif(units>100 and units<=200):
    bill=500+(units-100)*7
elif(units>200):
    bill=1200+(units-200)*10

print(f"Bill for this month={bill}")