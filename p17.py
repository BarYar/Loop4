l1=input("הכנס רשימה, שים רווחים בין המשתנים").split()
l2=input("הכנס רשימה, שים רווחים בין המשתנים").split()


b=False
for i in range (0,len(l1)):
    for j in range (0,len(l2)):
        if( l1[i] == l2[j]):
            b=True
            print("true")
            break

if(b==False):
    print(b)