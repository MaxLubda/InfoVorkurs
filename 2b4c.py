l = []
b = 121
while (b > 110):
    a = input("Zahl eingeben")
    a = float(a)
    l.append(a)
    b = input("noch eine Zahl?(y für yes oder n für nein)")
    b = ord(b)

print(sum(l)/len(l))
    
