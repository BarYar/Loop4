grade=int(input("Type 10 grades "))
wc=0
sum=0
gc=0
max=0
if((grade>100)or(grade<0)):
    wc+=1
    print("Type correct number.")
else:
    sum=sum+grade
    max=grade
    gc=gc+1
while ((wc<5) and (gc<10)):
    grade= int(input())
    if ((grade > 100) or (grade < 0)):
        wc=wc+1
        print("Type correct number.")
    else:
        sum = sum + grade
        if(grade>max):
            max=grade
        gc =gc+1
avg=sum/10
if (wc!=5):
    print ("The max:",max,"The avg:",avg)
else:
    print("error")



