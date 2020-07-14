#מקבלת מספר ומחזירה אותו הפוך וכפול 2
from Loop4Ex2 import C
num=int(input("input a number."))
s=C.CountZ(num)
tend=C.Tenz(s)
tenm=1
onum=0
while(s>=1):
    onum=int(onum+int(num/tend)*tenm)
    num=int(num%tend)
    tend=tend/10
    tenm=tenm*10
    s-=1
print ("The Opposite number is:",onum)