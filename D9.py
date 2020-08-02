#Write a Python program to remove duplicate values from a Dictionary.
#Write a python program that creates a dictionary. Then it will create a new dictionary that will swap the keys and values in a dictionary (the key will become a value and vice versa)
#Write a python program that creates a dictionary that contains 5 names of students and their grades (name=key, grade=value). The program will then calculate the average grade of the students. Then it will create a list with the names of the students that has grades higher than the average.
import math
def p9(d):
    t=False
    di={}
    for i in  d:
        for j in di:
            if (d[i]==di[j]):
                t=True
        if(t==False):
            di[i]=d[i]

    print (di)
def p10(d):
    di={}
    for i in d:
        di[d[i]]=i
    print(di)
def p11():
    d={}
    sum=0
    for i in range (0,5):
        name=input("הכנס את השם.")
        grade=int(input("הכנס את הציון."))
        sum=sum+grade
        d[name]=grade
    avg=sum/5
    l=[]
    for i in d:
        if (d[i]>avg):
            l.append(i)
    print (l)
def polyndrom(s):
    l=len(s)
    if ((l>=0)and(l<=1)):
        return True
    elif (s[0]==s[len(s)-1]):
        s=s[1:len(s)-1]
        return polyndrom (s)
    else:
        return False
def poly(s):
    b=True
    if len(s)%2==0:
        for i in range (0,int(len(s)/2)):
            if (s[i]!=s[len(s)-1-i]):
                b=False
                break
    else:
        for i in range (0,int(len(s)/2)+1):
            if (s[i]!=s[len(s)-1-i]):
                b=False
                break
    return b



#main
d={3:4,5:6,7:8,4:4}
s1="abcba"
s2="abccba"
s3="abcd"
s4="abca"
s5="abcra"
print(polyndrom(s1))
print(polyndrom(s2))
print(polyndrom(s3))
print(polyndrom(s4))
print(polyndrom(s5))
print(poly(s1))
print(poly(s2))
print(poly(s3))
print(poly(s4))
print(poly(s5))

