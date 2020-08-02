#מקבל List ומספר נוסף ומוציא אותו
def Rem(l,num):
    for i in range (0,len(l)):
        if (l[i]==num):
            l=l[:i]+l[i+1:]
            break

    return l
#מוסיף מספר לליסט
def Ad(l,num):
    l=l+[num]
    return l
#מחזירה את מיקום של האות הראשונה שהיא מקבלת
def fnd (l,c):
    for i in range (0, len (l)):
        if(l[i]==c):
            return i
    return -1


#main
l=[4,5,6,7,8,9,10,5]
print(Rem(l,5))
print (Ad(l,20))
print (Leng(l))
