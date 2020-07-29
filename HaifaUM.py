#שאלה 2 אוניבירסיטת חיפה-תוכנית שמדפיסה משולש שווה צלעות לפי הגובה
def updateUp(l,num):
#תוכנית המעדכנת רשימה
    for i in range (0,len(l)):
        if (l[i]!=" "):
            if (i<len(l)-2):
                l[i-1]=l[i]
            else:
                l[i-1]=l[i]
                l[i]=num
def printL(l):
#תוכנית המדפיסה רשימה
    for i in range (0,len(l)):
        if (i<len(l)-1):
            print(l[i],end='')
        else:
            print (l[i])
def updateDown (l):
#תוכנית המעדכנת בירידה את הרשימה
    num1=1
    num2=1
    for i in range (0,len(l)):
        if (l[i]!=" "):
            if l[i] == 1:
                l[i] = " "
            else:
                num2=l[i]
                l[i]=num1
                num1=num2



def eTringle(h):
    l=[]
    for i in range (0,h):
       if(i<h-1):
           l.append(" ")
       else:
           l.append(1)
    printL(l)
    num=2
    for i in range (0,len(l)-1):
        updateUp(l,num)
        printL(l)
        num+=1
    num-=2
    for i in range (0,len(l)-1):
        updateDown(l)
        printL(l)
        num -= 1



#main
eTringle(5)





