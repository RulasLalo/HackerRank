N= int(input())
lista=[]
for i in range(1,N+1):
    txt=input().split()
    if txt[0]=="insert":
        lista.insert(int(txt[1]),int(txt[2]))
    if txt[0]=="print":
        print(lista)
    if txt[0]=="remove":
        lista.remove(int(txt[1]))
    if txt[0]=="append":
        lista.append(int(txt[1]))
    if txt[0]=="sort":
        lista.sort()
    if txt[0]=="pop":
        lista.pop()
    if txt[0]=="reverse":
        lista.reverse()
