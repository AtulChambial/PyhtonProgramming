#Example : Creating set
# myset={'apple','cherry','mango'}
# print(myset)

#Example : Accessing items from set
# myset={'apple','cherry','mango'}
# for i in myset:
#     print(i)

#Example : value exists in set or not
# myset={'apple','cherry','mango'}
# print('mango'in myset)      #True
# print('banana'in myset)     #False

#Example4 : adding items to the set
#add()  update()
# myset={'apple','cherry','mango'}
# myset.add('lychee')
# #myset.update(["grapes","carrot"])
# print(myset)        #('apple', 'banana', 'mango', 'lychee', 'cherry', 'guava')

#Example5 : finding number of items in a set
# myset={'apple','cherry','mango'}
# print(len(myset))       #3

#Example6 : remove items from set
# myset={'apple','cherry','mango'}
# myset.remove('apple')    # remove fuction throws error while deleting non existing value
# myset.discard('apple')   #same as remove only diff is discard will not throw error while deleting non value element
# print(myset)        #{'cherry', 'mango'}

#Example7 :  clear all items from set
# myset={'apple','cherry','mango'}
# myset.clear()
# print(myset)        #set()

# del myset
# print(myset)        #NameError: name 'myset' is not defined

#Example8 : joining/combining sets
#myset1={'apple','cherry','mango'}
#myset2={'1','2','3'}
# myset3=myset1.union(myset2)
# print(myset3)       #{'mango', '3', 'cherry', '2', '1', 'apple'}

#update
#myset1.update(myset2)
#print(myset1)       #{'1', '3', '2', 'mango', 'apple', 'cherry'}





