n=int(input())
lista=[]
students={}

if n<=10:
   for i in range(1,n+1):
        datos=input().split()
        lista.append(datos)
        #break

for j in range(len(lista)):
    clave=lista[j][0]
    ind=[]
    #print("clave ",clave)
    for k in range(1,len(lista[j])):
        indice=lista[j][k]
        #print("indice ", indice)
        ind.append(indice)
    #print(ind)
    students[clave]=ind    
#print(students)

nombre=input()

#print(students[nombre])

suma=0
for i in students[nombre]:
    suma=float(i)+suma
    #print(i)
average=suma/3
print("%.2f"%average)
