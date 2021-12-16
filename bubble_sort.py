#Python code for bubble sort
l=[12,3,4,5,90,100,20,30,40]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print (l)
