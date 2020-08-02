# import random
# #19
# def p19():
#     l=[]
#     d={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
#     for i in range (0,10):
#         num=random.randint(1,9)
#         print(num)
#         l.append(num)
#         d[num]=d[num]+1
#     print(d)
#
# def p18(st1,st2,st3,st4,st5):
#     l=[st1,st2,st3,st4,st5]
#     c=""
#     c1=""
#     count=0
#     for i in range (0,5):
#         for j in range (0,len(l[i])):
#             if (j==0):
#                 c=l[i][j]
#             elif(j==len(l[i])-1):
#                 c1=l[i][j]
#         if((c==c1)and(len(l[i])>=4)):
#             count=count+1
#     print(count)
#
#
#
#
# # main
# p18("abcda","1231","121","abcde","aba")
# l=[1,2,3,4,5]
# l1=l[1:4]
# l2=l1.copy()
# l2.append(6)
# print(l1,l2)
# st="asfba"
# l=list(st)
# print(l)
# l=[1,2,3,4,5]
# for  in l:
#     print(i)
#     l=l+[1]
#     i=i+1
# print (l)


