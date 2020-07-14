#xפונקציה שבודקת ם y חיובי וקטן מ
def minp (x,y):
    if (x>0):
        if(x<y):
            return True
        else:
            return False
#main
Pos=False
num=int(input("print a number."))
while(num<=0):
    if (num == 0):
        break
    num = int(input("print a positive number."))

if(num!=0):
    Pos = True
    x=int(input("print a number."))
    while (x!=0):
            if(x>0):
                if(minp(x,num)==True):
                    num=x
            x = int(input("print a number."))

if(Pos==False):
    print("There is no positive number.")
else:
    print ("The minimum positive number is:",num)