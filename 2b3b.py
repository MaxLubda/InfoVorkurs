from 2b3.py import *
n = int(n)
text = input("Chiffrierten Text eigeben")
list = []
for i in text:
    b=ord(i)- n
    c=chr(b)
    list.append(c)
print(''.join(list))
