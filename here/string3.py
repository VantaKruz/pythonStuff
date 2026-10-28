textInp=input("Enter a string: ")
i=1
text=""
for x in textInp:
    y=x
    if(i%3==0):
        text=textInp.replace(y," ")
    i+=1
print(text)