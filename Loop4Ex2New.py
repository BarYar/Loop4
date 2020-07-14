#פונקציה שבודקת את כמות הספרות של המספר.
class C:
    def CountZ (num):
        i=1
        while((num>10)or(num<-10)):
            num=int(num/10)
            i+=1
        return i
    #פונקציה שמקבלת את כמות הספרות של המספר ומחזירה אותו בכפולות של 10.
    def Tenz(num):
        i=1
        for number in range(0,num-1):
            i=i*10
        return i

# main-מדפיס את הספרה השמאלית
num = int(input("Input a number."))
i = C.CountZ(num)
i = C.Tenz(i)
print("The left number is:.", int(num / i))
