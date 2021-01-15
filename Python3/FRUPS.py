#Find the Runner-Up Score! program

n=int(input())
lista=[]
unico=[]


datos=input()
lista= [int(d) for d in datos.split()]

lista.sort()

for i in lista:
    if i not in unico:
           unico.append(i)
       
#print(unico)
unico[-2:-1]
for i in unico[-2:-1]:
    print(i)
