#Approach1: Temporary variable
# mylist=[10,15,11,35,40]
# size=len(mylist)
# temp=0
# temp=mylist[0]
# mylist[0]=mylist[size-1]
# mylist[size-1]=temp
#
# print(mylist)

#Approach2: without Temporary variable
# mylist=[10,15,11,35,40]
# mylist[0],mylist[-1]=mylist[-1],mylist[0]
# print(mylist)

#Approach3: using tuple
mylist=[10,15,11,35,40]  #packing
print(mylist)
pos1,pos2=1,3
get=(mylist[pos1],mylist[pos2])  #unpacking
(mylist[pos2],mylist[pos1]) = get
print(mylist)

#Approach4: using * operand
# mylist=[10,15,11,35,40]
# start,*middle,end=mylist
# mylist=[end,*middle,start]
#
# print(mylist)

#Approach5: using pop() function
# mylist=[10,15,11,35,40]
#
# first=mylist.pop(0)
# last=mylist.pop(-1)
#
# mylist.insert(0,last)
# mylist.append(first)
# print(mylist)

