#חילוק ושארית
def divandmod():
    num1=int(input("Type 2 numbers."))
    num2 = int(input())
    while(num1<num2):
        num1 = int(input("Type 2 numbers,first 1 need to be bigger."))
        num2 = int(input())
    num2c=num2
    div=1
    while (num2c+num2<num1):
        div+=1
        num2c=num2c+num2

    mod=num1-num2c
    print ("The div is:",div,"The mod is:",mod)
#main
divandmod()
