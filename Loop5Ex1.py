width=int(input("Type The width and the length of the rectangle"))
length= int(input())
for j in range (0,length):
    for i in range (0,width):
        if((j==0)or(j==length-1)):
            if(i!=width-1):
                print ("*",end=' ')
            else:
                print ("*")
        elif(i==0):
            print ("*",end=' ')
        elif(i==width-1):
            print("*")
        else:
            print(" ",end=' ')
