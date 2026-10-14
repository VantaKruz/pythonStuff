print("Enter first time stamp")
H1=int(input("Enter Hour number: "))
M1=int(input("Enter Minute number: "))
S1=int(input("Enter Second number: "))
print("Enter second time stamp")
H2=int(input("Enter Hour number: "))
M2=int(input("Enter Minute number: "))
S2=int(input("Enter Second number: "))

H=H2-H1
M=M2-M1
S=S2-S1

Hsec=H*3600
Msec=M*60

TotalSec=S+Msec+Hsec

print(f"Seconds difference= {TotalSec}")