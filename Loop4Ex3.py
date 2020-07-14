#מקבלת 7 מספרים ומדפיסה את המספר הסידורי של הגדול מביניהם בלי רשימה
def maxS():
    num=int(input("Input 7 numbers."))
    i=1
    s=1
    for number in range(0,6):
        x=int(input())
        i += 1
        if(x>num):
            num=x
            s=i
    print ("The max number serial number is:",s)
#
#main
maxS()