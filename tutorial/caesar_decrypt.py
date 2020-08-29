d=input("Enter the Secret message")
m=''
for char in d:
    if char==' ':
        m=m+' '
    else:
        m=m+chr(ord(char)-3)
print(m)