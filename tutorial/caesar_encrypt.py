m=input("Enter the message")
d=''
for char in m:
    if char==' ':
        d=d+' '
    else:
        d=d+chr(ord(char)+3)
print(d)