n = input("wie viel?")
n = int(n)
l = []
for i in range(1,n+1,1):
   l.append(i)

for i in range (1,n+1,1):
   l2 = [i*g for g in l]
   print(l2)
