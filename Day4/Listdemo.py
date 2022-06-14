#Example1 : How to create list
# mylist=[10,20,30,40]
# mylist2=["apple","banana","orange","melon"]
# mylist3=["apple",10,"cherry",300]
# mylist4=()   #empty list
#
# print(mylist)
# print(mylist2)
# print(mylist3)
# print(mylist4)

#Example2 : Accessing items from the list
# mylist=["apple","banana","orange","melon"]  #Index starts from 0
#
# print(mylist[3])
# print(mylist[-1])   #-1 print last value

#Example3 : Range of Indexes
# mylist=["apple","banana","orange","melon","kiwi","mango","Lychee"]
# print(mylist[2:5])  #['orange', 'melon', 'kiwi']
# print(mylist[2:-1]) #['orange', 'melon', 'kiwi', 'mango']

#Example4 " Change item value
# mylist=["apple","banana","orange","melon","kiwi","mango","Lychee"]
# print(mylist)
# mylist[0]="Guava"
# print(mylist)    #['Guava', 'banana', 'orange', 'melon', 'kiwi', 'mango', 'Lychee']

#Example5 : Read item using loop statement
# mylist=["apple","banana","orange","melon","kiwi","mango","Lychee"]
# for i in mylist:
#     print(i)

#Example6 : check if item is available in list or not
# mylist=["apple","banana","orange","melon","kiwi","mango","Lychee"]
#
# if "aa" in mylist:
#     print("present")
# else:
#     print("Absent")

#Example7 : List Length (Counting number of items in a List)
# mylist=["apple","banana","orange","melon","kiwi","mango","Lychee"]
#
# print(len(mylist))

#Example8 : Add item  append()  insert()
# mylist=["apple","banana","orange","melon"]
# mylist.append("carrot")
# print(mylist)
# mylist.insert(1,"grapes")
# print(mylist)

#Example9 Remove items from the list
#pop
"""mylist=["apple","banana","orange","melon"]
mylist.pop(1)
print(mylist)   #['apple', 'orange', 'melon']"""

#del
# mylist=["apple","banana","orange","melon"]
# del mylist[0]
# print(mylist)  ['banana', 'orange', 'melon']

#clear
# mylist=["apple","banana","orange","melon"]
# mylist.clear()
# print(mylist)   #[]

#Example10 Copy List
# mylist1=["apple","banana","orange","melon"]
# mylist2=list(mylist1)
# print(mylist1)        #['apple', 'banana', 'orange', 'melon']
# print(mylist2)        #['apple', 'banana', 'orange', 'melon']

#copy
# mylist1=["apple","banana","orange","melon"]
# mylist2=mylist1.copy()
# print(mylist1)        #['apple', 'banana', 'orange', 'melon']
# print(mylist2)        #['apple', 'banana', 'orange', 'melon']

#Example11 Combine/Join Lists
# Using + operator
# list1=["a","b","c"]
# list2=[1,2,3]
# list3=list1+list2
# print(list3)       #['a', 'b', 'c', 1, 2, 3]
#using looping statement
# list1=["a","b","c"]
# list2=[1,2,3]
#
# for i in list2:
#     list1.append(i)
# print(list1)         #['a', 'b', 'c', 1, 2, 3]

#using extend function
# list1=["a","b","c"]
# list2=[1,2,3]
# list1.extend(list2)
# print(list2)

#Tuple
#Example1 Creating Tuple

# mytuple=("apple","banana","mango")
# print(mytuple)
# mytuple=()  #Empty Tuple

#Example2 Tuple :Accessing Tuple Items
# mytuple=("apple","banana","mango")
# print(mytuple[1])  #banana   here Index starts from 0

#Example4 Changing tuple items
#by default tuple does not allow to change values because it is immutable
#but there is workaround
#tuple--> list(modify)--> tuple

# mytuple=("apple","banana","mango")
# mylist=list(mytuple)
# mylist[0]="orange"
# mytuple=tuple(mylist)
# print(mytuple)

#Example5 Reading Tuple items using a loop
# mytuple=("apple","banana","mango")
#
# for i in mytuple:
#     print(i)

#Example6 : Check if item exists (searching for item in tuple)

# mytuple=("apple","banana","mango")
#
# if "apple" in mytuple:
#     print("present")
# else:
#     print("no")

#Example7 : counting Items in tuple
# mytuple=("apple","banana","mango")
# print(len(mytuple))  #3

#Example8 : copy the tuple
# mytuple=("apple","banana","mango")
# mytuple2=(mytuple)
# print(mytuple2)   ('apple', 'banana', 'mango')

#Example9 : removing items from tuple - not supported because tuple in immutable
mytuple=("apple","banana","mango")
#mytuple.remove("apple")           #Invalid
# del mytuple
# print(mytuple)    #NameError: name 'mytuple' is not defined.

#Example10: Joining/Combning Tuple
mytuple1=("apple","banana","mango")
mytuple2=("lychee","cherry","guava")
mytuple3=mytuple1+mytuple2
print(mytuple3)









