y=input("enter the file name")
a=open(y,"r")
list=[]
list=a.read()
list=list.split(" ")
for x in range(len(list)):
    list[x]=float(list[x])
print("file =",list)    
print("maximum number from the file =",max(list))
print("minimum number from the file =",min(list))
print("average from the file=",(sum(list)/2))