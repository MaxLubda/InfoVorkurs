n = input("Verschiebungsoffset eingeben")
n = int(n)
a = input("Zu verschlüsselnder Text eingeben")
list = []
for i in a:
    b=ord(i)+n
    c=chr(b)
    list.append(c)
print(''.join(list))
