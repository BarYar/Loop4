dic={}
sum=0
for i in range (0,5):
    name=input("type the name")
    grade=int(input("type the grade"))
    dic[name]=grade
    sum=sum+grade
avg=int(sum/5)
l=[]
for i in dic:
    if(dic[i]>avg):
        l.append(i)
print (l)





