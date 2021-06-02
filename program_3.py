a=open("file_a.txt","r")
b=open("file_b.txt","r")
c=a.read()
d=b.read()
c=c.split(" ")
d=d.split(" ")
for x in range(len(c)):
    c[x]=int(c[x])
for x in range(len(d)):
    d[x]=int(d[x])
print("number of element in file_1 is",len(c))   
print("number of element in file_2 is",len(d))    
print("sorted numbers in file_1",sorted(c))
print("sorted numbers in file_2",sorted(d))


