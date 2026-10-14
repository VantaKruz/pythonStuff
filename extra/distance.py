import math;

X1=int(input("Enter X Coordinate of 1st Vertex: "))
Y1=int(input("Enter Y Coordinate of 1st Vertex: "))
X2=int(input("Enter X Coordinate of 2nd Vertex: "))
Y2=int(input("Enter Y Coordinate of 2nd Vertex: "))

d=math.sqrt((X2-X1)*(X2-X1)+ (Y2-Y1)*(Y2-Y1))

print(f"Distance between ({X1},{Y1}) and ({X2},{Y2}) is {d}")