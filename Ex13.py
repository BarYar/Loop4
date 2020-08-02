#Create a list of 20 random numbers between 1 and 100 and write a program
#that will remove all items in the list that equals a certain number. This
#number will be given by the user as an input.42
import random
l=[]
b=False
for i in range (0,20):
   l.append(random.randint(0,100))
print(l)
num=int(input("הכנס מספר."))
for i in range(0,len(l)):
    if (l[i]==num):
        b=True
        break
if(b==True):
    print(b)
else:
    print(b)


