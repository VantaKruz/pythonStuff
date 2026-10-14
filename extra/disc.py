price1=int(input("Enter price of first product: "))
price2=int(input("Enter price of second product: "))
price3=int(input("Enter price of third product: "))

total=price1+price2+price3
discount=0
if(total>1000):
    discount=0.1*total
total-=discount
print(f"Discount={discount}, Final Price={total}")