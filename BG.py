# def count(L):
#     print(_count(L,0,0))
# def _count(l,i,sum):
#     if(i==len(l)-1):
#         sum1=sum
#         sum1=sum1+l[i]
#         sum=sum-l[i]
#         if((sum1==0)or(sum==0)):
#             return 1
#         else:
#             return 0
#     if(i<len(l)):
#         return _count(l, i + 1, sum+l[i]) + _count(l, i + 1, sum-l[i])
def solve(L):
    s=[]
    b=_solve(L,s,0,0)
    if(b):
        return s
    else:
        return None
def _solve(l,s,i,sum):
    exist1=False
    exist2=False
    if(i==len(l)-1):
        sum1=sum
        sum1=sum1+l[i]
        sum=sum-l[i]
        if(sum1==0):
            s.append(1)
            return True
        if(sum==0):
            s.append(-1)
            return True
        else:
            return False
    if(i<len(l)-1):
        s1=s.copy()
        s2=s.copy()
        exist1=_solve(l,s1,i+1,sum+l[i])
        exist2=_solve(l,s2,i+1,sum-l[i])
        if (exist1):
            s=s1
            s.append(1)
            return True
        elif(exist2):
            s=s2
            s.append(-1)
            return True
        else:
            return False
    if exist1 or exist2:
        return True
    else:
        return False


#main
l=[5,4,1]
print(solve(l))