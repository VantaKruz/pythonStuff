price=int(input("Enter price amount: "))
disc=0
if(price<=500):
    disc=0
elif(price>500 and price<=1000):
    disc=0.1*price
elif(price>1000):
    disc=0.2*price

bill=price-disc

print(f"Discount={disc},Final Price={bill}")