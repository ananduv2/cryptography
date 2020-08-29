m=input("Enter the plain text: ")
m=m.replace(" ","")
m=m.upper()
n=[""]*3
i=0
for char in m:
    n[i]=n[i]+char
    if i>=2:
        i=0
    else:
        i=i+1
d="".join(n)
print(d)