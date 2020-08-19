N = int(input())
l=[]
for i in range(N):
    x=input().spilt()
    if x[0]=="insert":
        l.insert(int(x[1]),int(x[2]))
    if x[0]=="append":
        l.append(int(x[1]))
    if x[0]=="remove":
        l.remove(int(x[1]))
    if x[0]=="sort":
        l.sort()
    if x[0]=="pop":
        if len(l)!=0:
            l.pop()
    if x[0]=="reverse":
        l.reverse()
    if x[0]=="print":
        print(int(l))
       
    
